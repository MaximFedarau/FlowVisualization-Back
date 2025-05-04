import subprocess
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException
from fastapi.responses import FileResponse

from app.utils.clear_dir import clear_dir


def generate_video():
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

    new_video = new_video_dir / f"{new_id}.mp4"
    command = f'manim -ql -o "{new_video.as_posix()}" \
    "{video_generator_file.as_posix()}" CreateCircle'

    try:
        subprocess.run(command, shell=True, check=False)  # noqa: S602
    except Exception as e:  # noqa: BLE001
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
