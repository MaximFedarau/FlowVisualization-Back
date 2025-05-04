from fastapi import APIRouter

from app.core.generate_video import generate_video

router = APIRouter()


@router.get("/download")
def download_video() -> dict:
    return generate_video()


@router.get("/link")
def get_video_link() -> dict:
    return {"data": "link"}
