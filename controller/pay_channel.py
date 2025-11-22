from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from service.pay_channel import (
    create_pay_channel,
    delete_pay_channel,
    update_pay_channel,
    get_pay_channel,
    get_pay_channel_by_channel_id,
    list_pay_channels
)
from models.pay_channel import PayChannel, PayChannelCreate, PayChannelUpdate
from pmf.models import Result

router = APIRouter(prefix="/paychannel")

@router.post("/save")
def create_channel(
    channel: PayChannelCreate
):
    """创建新的支付渠道"""
    return Result.success(data=create_pay_channel(channel.dict()))

@router.get("/get")
def read_channel(
    id: Optional[int] = Query(0, description="ID"),
    channel_id: Optional[str] = Query(None, description="渠道ID")
):
    """获取单个支付渠道"""
    if id > 0:
        return get_pay_channel(id=id)
    elif channel_id:
        return get_pay_channel_by_channel_id(channel_id=channel_id)
    else:
        return Result.error(msg="id or channel_id must be provided")


@router.post("/update")
def update_channel(
    channel: PayChannelUpdate
):
    """更新支付渠道"""
    db_channel = update_pay_channel(channel_id=channel.channel_id, channel_data=channel.dict(exclude_unset=True))
    if db_channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    return Result.success(data=db_channel)

@router.post("/del")
def delete_channel(
    channel_id: str = Query(..., description="渠道ID")
):
    """删除支付渠道"""
    if not delete_pay_channel(channel_id=channel_id):
        raise HTTPException(status_code=404, detail="Channel not found")
    return Result.success(msg="Channel deleted successfully")
@router.get("/list")
def list_channels(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    channel_type: Optional[str] = Query(None),
    service_name: Optional[str] = Query(None)
):
    """获取支付渠道列表"""
    l = list_pay_channels(
        skip=skip,
        limit=limit,
        channel_type=channel_type,
        service_name=service_name
    )
    return Result.success(data=l)
