from pydantic import BaseModel
from app.models.graph import Edge

class Action(BaseModel):
    way : list[Edge]
    flow : int

class Visualization(BaseModel):
    visualization : list[Action]
    flow : int