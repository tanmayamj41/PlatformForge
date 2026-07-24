from uuid import uuid4

from fastapi import APIRouter

from app.schemas.project import Project, ProjectCreate

router = APIRouter(prefix="/api/v1/projects", tags=["Projects"])

projects: list[Project] = []


@router.post("/", response_model=Project)
async def create_project(project: ProjectCreate):
    new_project = Project(
        id=uuid4(),
        name=project.name,
        description=project.description,
    )

    projects.append(new_project)
    return new_project


@router.get("/", response_model=list[Project])
async def get_projects():
    return projects
