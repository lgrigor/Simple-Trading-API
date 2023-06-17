import asyncio
import random

from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from fastapi.responses import Response

from ..database.data import order_db
from ..utils.miscellaneous import change_order_status_to_executed
from ..utils.miscellaneous import generate_order_id
from ..utils.miscellaneous import notify_clients

router = APIRouter()


@router.get("/")
async def home_page():
    return FileResponse(r"app/templates/index.html")


@router.get("/orders")
async def get_orders():
    await asyncio.sleep(random.uniform(0.1, 1.0))
    return list(order_db.values())


@router.get("/orders/{order_id}")
async def get_order_with_id(order_id: int):
    await asyncio.sleep(random.uniform(0.1, 1.0))
    if order_id in order_db:
        return order_db[order_id]
    else:
        return JSONResponse(status_code=404, content={"code": 404, "message": "Order not found"})


@router.post("/orders")
async def place_a_new_order(order_info: dict):
    if ("stocks" not in order_info) or (not order_info["stocks"]):
        return JSONResponse(status_code=400, content={"code": 400, "message": "Missing stocks"})

    if ("quantity" not in order_info) or (order_info["quantity"] <= 0):
        return JSONResponse(status_code=400, content={"code": 400, "message": "Missing quantity"})

    if len(order_info) != 2:
        del order_info["stocks"]
        del order_info["quantity"]
        return JSONResponse(status_code=400, content={"code": 400, "message": f"Redundant properties - {list(order_info.keys())}"})

    await asyncio.sleep(random.uniform(0.1, 1.0))

    order_id = await generate_order_id()
    order_status = "PENDING"

    await notify_clients(order_id, order_status)
    asyncio.create_task(change_order_status_to_executed(order_id))

    curr_order = dict()
    curr_order["id"] = order_id
    curr_order.update(order_info)
    curr_order["status"] = order_status

    order_db[order_id] = curr_order

    return JSONResponse(status_code=201, content=curr_order)


@router.delete("/orders/{order_id}")
async def cancel_order_with_id(order_id: int):
    await asyncio.sleep(random.uniform(0.1, 1.0))
    if order_id in order_db:
        order_db[order_id]["status"] = "CANCELLED"
        await notify_clients(order_id, "CANCELLED")
        return Response(status_code=204)
    else:
        return JSONResponse(status_code=404, content={"code": 404, "message": "Order not found"})
