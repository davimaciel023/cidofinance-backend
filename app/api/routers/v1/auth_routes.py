from fastapi import APIRouter

auth_router = APIRouter(prefix="/api/v1/auth", tags=["Gestão de Autenticação"])

@auth_router.get("/login")
async def login():
    return