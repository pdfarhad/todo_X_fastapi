# generated by datamodel-codegen:
#   filename:  oas.yaml
#   timestamp: 2022-09-30T12:49:38+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra


class Error(BaseModel):
    detail: Optional[str] = None


class Priority(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class Status(Enum):
    pending = 'pending'
    progress = 'progress'
    completed = 'completed'


class CreateTaskSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    priority: Optional[Priority] = 'low'
    status: Optional[Status] = 'pending'
    task: str

class GetTaskSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    id: UUID
    created: datetime
    priority: Priority
    status: Status
    task: str


class ListTasksSchema(BaseModel):
    tasks: List[GetTaskSchema]
