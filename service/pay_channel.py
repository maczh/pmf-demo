from typing import List, Optional
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.pay_channel import PayChannel
from pmf.core import app as PMFApp
from common.vars import global_vars

db = global_vars.app.client.mysql.get_session()

def create_pay_channel(channel_data: dict) -> PayChannel:
    """创建新的支付渠道"""
    channel_data['create_time'] = datetime.now()
    db_channel = PayChannel(**channel_data)
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel

def delete_pay_channel(channel_id: str) -> bool:
    """删除支付渠道"""
    db_channel = db.query(PayChannel).filter(PayChannel.id == channel_id).first()
    if db_channel:
        db.delete(db_channel)
        db.commit()
        return True
    return False

def update_pay_channel(channel_id: str, channel_data: dict) -> Optional[PayChannel]:
    """更新支付渠道"""
    db_channel = db.query(PayChannel).filter(PayChannel.id == channel_id).first()
    if db_channel:
        channel_data['update_time'] = datetime.now()
        for key, value in channel_data.items():
            setattr(db_channel, key, value)
        db.commit()
        db.refresh(db_channel)
        return db_channel
    return None

def get_pay_channel(id: int) -> Optional[PayChannel]:
    """获取单个支付渠道"""
    return db.execute(select(PayChannel).where(PayChannel.id == id)).scalar_one_or_none()

def get_pay_channel_by_channel_id(channel_id: str) -> Optional[PayChannel]:
    """通过渠道ID获取支付渠道"""
    return db.execute(select(PayChannel).where(PayChannel.channel_id == channel_id)).scalar_one_or_none()

def list_pay_channels(
    skip: int = 0,
    limit: int = 100,
    channel_type: Optional[str] = None,
    service_name: Optional[str] = None
) -> List[PayChannel]:
    """获取支付渠道列表"""
    query = db.query(PayChannel)
    
    if channel_type:
        query = query.filter(PayChannel.type == channel_type)
    if service_name:
        query = query.filter(PayChannel.service_name == service_name)
        
    return query.offset(skip).limit(limit).all()
