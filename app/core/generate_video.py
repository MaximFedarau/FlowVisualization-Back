import json
import subprocess
from pathlib import Path
from uuid import uuid4

import cloudinary
import cloudinary.uploader
from fastapi import HTTPException
from fastapi.responses import FileResponse

from app.config import settings
from app.core.generate_edmonds_karp_visualization import generate_visualization
from app.models.picture import Picture
from app.utils.clear_dir import clear_dir


def generate_video_file(graph: Picture) -> FileResponse:
    """Generate video file."""
    filepath = Path(__file__)
    root_dir = Path(Path(filepath.parent / "../..").resolve())

    videos_dir = root_dir / "videos"
    videos_dir.mkdir(exist_ok=True)

    new_id = uuid4()
    new_video_dir = videos_dir / str(new_id)
    new_video_dir.mkdir()

    template_file = (root_dir / "app/utils") / "generate_manim.py"
    video_generator_file = new_video_dir / f"{new_id}.py"
    video_generator_file.write_bytes(template_file.read_bytes())

    data_file = new_video_dir / "data.json"
    data = graph.model_dump()

    visualization = generate_visualization(graph.graph)
    data["visualization"] = visualization.model_dump()["visualization"]
    data["edges"] = data["graph"]["edges"]
    data_file.write_text(json.dumps(data))

    new_video = new_video_dir / f"{new_id}.mp4"
    command = f'VISUALIZATION_DATA_PATH="{data_file.as_posix()}" manim -ql -o "{new_video.as_posix()}" \
    "{template_file.as_posix()}" CreateFlow'

    try:
        subprocess.run(command, shell=True, check=False)
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f"Video generation failed: {e!s}",
        ) from None
    finally:
        media_dir = root_dir / "media"
        if media_dir.exists():
            clear_dir(media_dir)

    return FileResponse(
        new_video.as_posix(),
        media_type="video/mp4",
        filename=f"{new_id}.mp4",
    )


def generate_video_link(graph: Picture) -> dict:
    """Upload video to cloud storage and return link."""
    video = generate_video_file(graph)
    cloudinary.config(
        cloud_name=settings.CLOUDINARY_CLOUD_NAME,
        api_key=settings.CLOUDINARY_API_KEY,
        api_secret=settings.CLOUDINARY_API_SECRET,
    )
    res = {"url": ""}
    try:
        res = cloudinary.uploader.upload_large(
            video.path,
            resource_type="video",
            public_id=f"FlowVisualization/ \
            {Path(video.filename if video.filename is not None else '').stem}",
        )
    except Exception as e:  # noqa: BLE001
        raise HTTPException(
            status_code=404,
            detail=f"Video uploading failed: {e!s}",
        ) from None
    finally:
        video_dir = Path(video.path).parent
        if video_dir.exists():
            clear_dir(video_dir)

    return {"url": res["url"]}
