from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

Base = declarative_base()

class PayOrder(Base):
    __tablename__ = 'pay_order'

    id = Column(BigInteger, primary_key=True)
    pay_order_id = Column(String(64), nullable=False, unique=True, comment='支付订单ID')
    title = Column(String(256), default='', comment='支付标题')
    describe = Column(String(256), default='', comment='支付描述')
    channel_id = Column(String(64), nullable=False, default='', comment='支付渠道ID')
    amount = Column(BigInteger, nullable=False, default=0, comment='支付金额')
    status = Column(String(32), nullable=False, default='', comment='支付状态')
    buyer_id = Column(String(64), nullable=False, default='', comment='买家用户ID')
    pay_app = Column(String(64), nullable=False, default='', comment='支付应用')
    qr_code = Column(String(256), nullable=False, default='', comment='支付二维码')
    bar_code = Column(String(256), nullable=False, default='', comment='支付条码')
    fail_reason = Column(String(256), nullable=False, default='', comment='支付失败原因')
    pay_time = Column(String(64), comment='支付时间')
    refunded = Column(Boolean, default=False, comment='是否已退款')
    refund_amount = Column(BigInteger, nullable=False, default=0, comment='退款金额')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')

class PayOrderBase(BaseModel):
    pay_order_id: str
    title: str = ''
    describe: str = ''
    channel_id: str
    amount: int
    status: str = ''
    buyer_id: Optional[str] = None
    pay_app: Optional[str] = None
    qr_code: Optional[str] = None
    bar_code: Optional[str] = None
    fail_reason: Optional[str] = None
    pay_time: Optional[str] = None
    refunded: Optional[bool] = None
    refund_amount: Optional[int] = None
    
class PayOrderCreate(PayOrderBase):
    pass

class PayOrderUpdate(PayOrderBase):
    pay_order_id:  Optional[str]  = None
    title:  Optional[str]  = None
    describe:  Optional[str]  = None
    channel_id:  Optional[str]  = None
    amount:  Optional[int]  = None
    status:  Optional[str]  = None
    buyer_id:  Optional[str]  = None
    pay_app:  Optional[str]  = None
    qr_code:  Optional[str]  = None
    bar_code:  Optional[str]  = None
    fail_reason:  Optional[str]  = None
    pay_time:  Optional[str]  = None
    refunded:  Optional[bool]  = None
    refund_amount:  Optional[int]  = None

class PayOrderResponse(PayOrderBase):
    id: int
    create_time: datetime
    update_time: Optional[datetime] = None
    
    class Config:
        from_attributes = True