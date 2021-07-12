from datetime import datetime
from enum import Enum

from app.api.v1.schemas.base import BaseEnhancedModel


class ETaskStatus(Enum):
    todo = "todo"
    doing = "doing"
    done = "done"


class TaskBase(BaseEnhancedModel):
    title: str
    detail: str
    start_date: datetime
    end_date: datetime
    color: str
    status: ETaskStatus


class TaskCreate(TaskBase):
    issue_id: str


class TaskUpdate(TaskBase):
    pass


class TaskSchema(TaskBase):
    id: int


class TaskMongoSchema(TaskBase):
    object_id: str
    issue_id: str
