import asyncio
import random

from fastapi import WebSocket
from starlette.websockets import WebSocketState

from ..database.data import connected_clients
from ..database.data import order_db


async def notify_clients(order_id: int, order_status: str, conn_clients=connected_clients):
    disconnected_clients = set()
    if conn_clients:
        message = f"Order {order_id} has been executed. Status: {order_status}"
        for client in conn_clients:
            client: WebSocket

            if client.client_state == WebSocketState.CONNECTED:
                await client.send_text(message)
            elif client.client_state == WebSocketState.DISCONNECTED:
                disconnected_clients.add(client)
            else:
                print("Unhandled state of WebSocket")
        conn_clients -= disconnected_clients


async def change_order_status_to_executed(order_id: int):
    await asyncio.sleep(random.randint(1, 5))
    order_db[order_id]["status"] = "EXECUTED"
    await notify_clients(order_id, "EXECUTED")


async def generate_order_id():
    order_id = random.randint(1, 1000)
    while order_id in order_db:
        order_id = random.randint(1, 1000)
    return order_id
