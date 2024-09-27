from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import api.schemas.task as task_schema

import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()


# @router.get("/tasks")
@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のToDoタスク")]


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_tasks(
    task_body: task_schema.TaskCreate, db: Session = Depends(get_db)
):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_tasks(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_tasks(task_id: int):
    pass
