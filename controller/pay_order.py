from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from service.pay_order import (
    create_pay_order,
    delete_pay_order,
    update_pay_order,
    get_pay_order,
    get_pay_order_by_order_id,
    list_pay_orders,
)
from models.pay_order import PayOrder, PayOrderCreate, PayOrderUpdate
from pmf.models import Result

router = APIRouter(prefix="/payorder")

@router.post("/save")
def create_order(
    order: PayOrderCreate
):
    """创建新的支付渠道"""
    return Result.success(data=create_pay_order(order.dict()))

@router.get("/get")
def read_order(
    id: Optional[int] = Query(0, description="ID"),
    order_id: Optional[str] = Query(None, description="订单ID")
):
    """获取单个支付渠道"""
    if id > 0:
        db_order = get_pay_order(id=id)
    elif order_id:
        db_order = get_pay_order_by_order_id(order_id=order_id)
    else:
        return Result.error(msg="id or order_id must be provided")
    return Result.success(data=db_order)


@router.post("/update")
def update_order(
    order: PayOrderUpdate
):
    """更新支付渠道"""
    db_order = update_pay_order(order_id=order.order_id, order_data=order.dict(exclude_unset=True))
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return Result.success(data=db_order)

@router.post("/del")
def delete_order(
    order_id: str = Query(..., description="渠道ID")
):
    """删除支付渠道"""
    if not delete_pay_order(order_id=order_id):
        raise HTTPException(status_code=404, detail="Order not found")
    return Result.success(msg="Order deleted successfully")
@router.get("/list")
def list_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    channel_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None)
):
    """获取支付渠道列表"""
    l = list_pay_orders(
        skip=skip,
        limit=limit,
        channel_id=channel_id,
        status=status
    )
    return Result.success(data=l)
