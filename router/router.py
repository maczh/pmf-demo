from fastapi import APIRouter
from controller.ums_store import router as ums_store_router
from controller.pay_channel import router as pay_channel_router
from controller.pay_order import router as pay_order_router
v1 = APIRouter(prefix="/api/v1")
v1.include_router(ums_store_router)
v1.include_router(pay_channel_router)
v1.include_router(pay_order_router)
