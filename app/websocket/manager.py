from fastapi import APIRouter
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from ..database.data import connected_clients

ws_router = APIRouter()


@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text("Received: " + data)
    except WebSocketDisconnect as e:
        print("WebSocket connection closed:", e.code)
