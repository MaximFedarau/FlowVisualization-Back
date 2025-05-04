from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.core.generate_video import generate_video_file, generate_video_link

router = APIRouter()


@router.get("/download")
def download_video() -> FileResponse:
    """Download video."""
    return generate_video_file()


@router.get("/link")
def get_video_link() -> dict:
    """Return link to video in cloud storage."""
    return generate_video_link()
