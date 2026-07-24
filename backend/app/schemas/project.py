from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    name: str
    description: str


class Project(ProjectCreate):
    id: UUID = Field(default_factory=uuid4)
