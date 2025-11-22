from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

Base = declarative_base()

# SQLAlchemy 模型 - 用于数据库操作
class PayChannel(Base):
    __tablename__ = 'pay_channel'

    id = Column(BigInteger, primary_key=True)
    channel_id = Column(String(64), unique=True, nullable=False, default='', comment='渠道ID')
    channel_name = Column(String(64), nullable=False, default='', comment='渠道名称')
    service_name = Column(String(64), nullable=False, default='', comment='支付通道服务名称')
    pay_uri = Column(String(255), default='', comment='支付通道支付接口URI')
    refund_uri = Column(String(255), default='', comment='支付通道退款接口URI')
    cancel_uri = Column(String(255), default='', comment='支付通道取消接口URI')
    query_uri = Column(String(255), default='', comment='支付通道查询接口URI')
    type = Column(String(20), nullable=False, comment='通道类型')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')

# Pydantic 模型 - 用于FastAPI请求和响应
class PayChannelBase(BaseModel):
    channel_id: str
    channel_name: str
    service_name: str
    pay_uri: str = ''
    refund_uri: str = ''
    cancel_uri: str = ''
    query_uri: str = ''
    type: str

class PayChannelCreate(PayChannelBase):
    pass

class PayChannelUpdate(BaseModel):
    channel_name: Optional[str] = None
    service_name: Optional[str] = None
    pay_uri: Optional[str] = None
    refund_uri: Optional[str] = None
    cancel_uri: Optional[str] = None
    query_uri: Optional[str] = None
    type: Optional[str] = None

class PayChannelResponse(PayChannelBase):
    id: int
    create_time: datetime
    update_time: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# 通道类型常量
class ChannelType:
    SCAN = "SCAN"
    QRCODE = "QRCODE"
    MINIPROGRAM = "MINIAPP"
