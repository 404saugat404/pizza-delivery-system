from fastapi import FastAPI
from authentication import authentication_router
from orders import order_router


app = FastAPI()
app.include_router(authentication_router)
app.include_router(order_router)