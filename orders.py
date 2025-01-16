from fastapi import APIRouter

order_router = APIRouter()

@order_router.get("/orders")
async def get_orders():
    return {"orders": "hello guys"}