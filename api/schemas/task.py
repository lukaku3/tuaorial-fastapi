import datetime
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, example="クリーニングを取りに行く")
    due_date: datetime.date | None = Field(None, example="2024-09-30")


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
