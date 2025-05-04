from fastapi import APIRouter, HTTPException

from app.constants.enums import AlgorithmEnum
from app.core.generate_video import generate_video_file, generate_video_link
from app.models.picture import Picture

router = APIRouter()


@router.post("/download/{algorithm_id}")
def download_video(graph: Picture, algorithm_id: str) -> None:
    """Download video."""
    if algorithm_id not in AlgorithmEnum:
        raise HTTPException(status_code=404)
    return generate_video_file(graph, AlgorithmEnum[algorithm_id])


@router.post("/link/{algorithm_id}")
def get_video_link(graph: Picture, algorithm_id: str) -> dict:
    """Return link to video in cloud storage."""
    if algorithm_id not in AlgorithmEnum:
        raise HTTPException(status_code=404)
    return generate_video_link(graph, AlgorithmEnum[algorithm_id])
