from pydantic import BaseModel
from typing import List

class Task(BaseModel):
      title:str
      is_completed:bool

class TaskList(BaseModel):
      tasks:List[Task]

class Ids(BaseModel):
      id:str

class TaskDeleteList(BaseModel):
      tasks:List[Ids]