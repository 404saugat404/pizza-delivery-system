from fastapi import APIRouter

authentication_router = APIRouter()

@authentication_router.get("/auth")
async def get_auth():
    return {"auth": "hello guys"}