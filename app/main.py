from fastapi import FastAPI

app = FastAPI(
    title="CIDO FINANCE API",
    version="0.1.0"
)

from app.api.routers.v1.auth_routes import auth_router

app.include_router(auth_router)
