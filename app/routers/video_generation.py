from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.core.generate_video import generate_video_file, generate_video_link
from app.models.picture import Picture

router = APIRouter()


@router.post("/download")
def download_video(graph: Picture) -> FileResponse:
    """Download video."""
    return generate_video_file(graph)


@router.post("/link")
def get_video_link(graph: Picture) -> dict:
    """Return link to video in cloud storage."""
    return generate_video_link(graph)
