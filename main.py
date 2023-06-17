from fastapi import FastAPI

from app.endpoints.order import router
from app.websocket.manager import ws_router

app = FastAPI()
connected_clients = set()
app.include_router(router)
app.include_router(ws_router)
