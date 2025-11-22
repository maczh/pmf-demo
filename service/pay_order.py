from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from models.pay_order import PayOrder

from common.vars import global_vars

db = global_vars.app.client.mysql.get_session()

def create_pay_order(order_data: dict) -> PayOrder:
    """创建新的支付订单"""
    db_order = PayOrder(**order_data)
    db_order.create_time = datetime.now()
    db_order.update_time = datetime.now()
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_pay_order(order_id: int) -> bool:
    """删除支付订单"""
    db_order = db.query(PayOrder).filter(PayOrder.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return True
    return False

def update_pay_order(order_id: int, order_data: dict) -> Optional[PayOrder]:
    """更新支付订单"""
    db_order = db.query(PayOrder).filter(PayOrder.id == order_id).first()
    if db_order:
        for key, value in order_data.items():
            setattr(db_order, key, value)
        db_order.update_time = datetime.now()
        db.commit()
        db.refresh(db_order)
        return db_order
    return None

def get_pay_order(id: int) -> Optional[PayOrder]:
    """获取单个支付订单"""
    return db.query(PayOrder).filter(PayOrder.id == id).first()

def get_pay_order_by_order_id(order_id: str) -> Optional[PayOrder]:
    """通过订单ID获取支付订单"""
    return db.query(PayOrder).filter(PayOrder.pay_order_id == order_id).first()

def list_pay_orders(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    channel_id: Optional[str] = None
) -> List[PayOrder]:
    """获取支付订单列表"""
    query = db.query(PayOrder)
    
    if status:
        query = query.filter(PayOrder.status == status)
    if channel_id:
        query = query.filter(PayOrder.channel_id == channel_id)
        
    return query.offset(skip).limit(limit).all()
