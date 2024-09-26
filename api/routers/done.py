from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_as_done(task_id: int):
    pass


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_as_done(task_id: int):
    pass
