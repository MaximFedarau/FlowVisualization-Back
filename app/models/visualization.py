from pydantic import BaseModel

from app.models.graph import Edge


class Action(BaseModel):
    """Action model."""

    way: list[Edge]
    flow: int


class Visualization(BaseModel):
    """Visualization model."""

    visualization: list[Action]
    flow: int
