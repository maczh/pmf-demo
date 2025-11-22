import sys
import os
# import etcd3
from pathlib import Path
from sqlalchemy import  text
from sqlalchemy.orm import  Session, declarative_base
# from router.router import v1

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# 添加项目根目录到Python路径
sys.path.append(str(Path(__file__).parent.parent))
# sys.path.append("D:\\Projects\\python")
from pmf.core import app as PMFApp
from pmf.models import Result
from pmf.middleware.postlog import LoggingMiddleware

from common.vars import global_vars

global_vars.app = PMFApp.App(config_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"kmp.yml"))
from fastapi import APIRouter
from controller.ums_store import router as ums_store_router
from controller.pay_channel import router as pay_channel_router
from controller.pay_order import router as pay_order_router
router = APIRouter(prefix="/api/v1")
router.include_router(ums_store_router)
router.include_router(pay_channel_router)
router.include_router(pay_order_router)


if __name__ == "__main__":
    # myapp = PMFApp.App(config_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"kmp.yml"))
    global_vars.app.app.add_middleware(LoggingMiddleware)
    global_vars.app.app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # myapp.app.include_router(router)
    global_vars.app.app.include_router(router)
    # PMFApp.app = myapp
    # global_vars.app = myapp
    global_vars.app.run()
    
