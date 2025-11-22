from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from service import ums_store as ums_store_service
from models.ums_store import UmsStore, UmsStoreCreate, UmsStoreUpdate
from pmf.models import Result

router = APIRouter(prefix="/umsstore")


@router.post("/create")
def create_ums_store(store: UmsStoreCreate):
    """创建ums_store"""
    return ums_store_service.create_ums_store(store=store)


@router.post("/delete")
def delete_ums_store(id: int) :
    """删除ums_store"""
    return ums_store_service.delete_ums_store(id=id)


@router.post("/update")
def update_ums_store(store: UmsStoreUpdate):
    """更新ums_store"""
    return ums_store_service.update_ums_store(store=store)


@router.get("/get")
def get_ums_store(id: Optional[int] = Query(0, description="ID"),
                 store_id: Optional[str] = Query(None, description="store_id")):
    """获取ums_store"""
    if id > 0:
        return ums_store_service.get_ums_store(id=id)
    elif store_id:
        return ums_store_service.get_ums_store_by_store_id(store_id=store_id)
    else:
        return Result.error(msg="id or store_id must be provided")
 


@router.get("/list")
def list_ums_stores():
    """获取ums_store列表"""
    return ums_store_service.list_ums_stores()
