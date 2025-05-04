from fastapi import APIRouter

from app.core.generate_video import generate_video_file, generate_video_link

router = APIRouter()


@router.get("/download")
def download_video() -> dict:
    return generate_video_file()


@router.get("/link")
def get_video_link() -> dict:
    return generate_video_link()
