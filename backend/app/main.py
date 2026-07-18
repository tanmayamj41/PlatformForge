from fastapi import FastAPI

app = FastAPI(
        title="PlatformForge API",
        description="Backend API for PlatformForge",
        version="0.1.0"
)

@app.get("/")
async def root():
        return {
        "project": "PlatformForge",
        "status": "running",
        "version": "0.1.0"
}
