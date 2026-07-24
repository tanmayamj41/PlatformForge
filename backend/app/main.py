from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.project import router as project_router

app = FastAPI(
        title="PlatformForge API",
        description="Backend API for PlatformForge",
        version="0.1.0"
)

app.include_router(health_router)
app.include_router(project_router)

@app.get("/")
async def root():
        return {
        "project": "PlatformForge",
        "status": "running",
        "version": "0.1.0"
}
