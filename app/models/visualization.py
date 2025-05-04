from pydantic import BaseModel, Field
from typing import List, Tuple
from app.models.graph import Edge

class Action(BaseModel):
    way : List[Edge]
    flow : int

class Visualization(BaseModel):
    visualization : List[Action]
    flow : int