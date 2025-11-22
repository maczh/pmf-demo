from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

Base = declarative_base()


class RefundOrder(Base):
    __tablename__ = 'refund_order'

    id = Column(BigInteger, primary_key=True)
    refund_order_id = Column(String(64), nullable=False, unique=True, default='', comment='退款订单ID')
    pay_order_id = Column(String(64), nullable=False, default='', comment='支付订单ID')
    refund_request_id = Column(String(64), nullable=False, default='', comment='退款请求ID')
    amount = Column(BigInteger, nullable=False, default=0, comment='退款金额')
    status = Column(String(32), default='', comment='退款状态')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')

class RefundOrderBase(BaseModel):
    refund_order_id: str
    pay_order_id: str
    refund_request_id: str
    amount: int
    status: str = ''
    
class RefundOrderCreate(RefundOrderBase):
    pass

class RefundOrderUpdate(RefundOrderBase):
    refund_order_id:  Optional[str]  = None
    pay_order_id:  Optional[str]  = None
    refund_request_id:  Optional[str]  = None
    amount:  Optional[int]  = None
    status:  Optional[str]  = None
    
class RefundOrderResponse(RefundOrderBase):
    id: int
    create_time: datetime
    update_time: Optional[datetime] = None

    class Config:
        from_attributes = True