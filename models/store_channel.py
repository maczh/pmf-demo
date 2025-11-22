from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

Base = declarative_base()

class StoreChannel(Base):
    __tablename__ = 'store_channel'

    id = Column(BigInteger, primary_key=True)
    store_id = Column(String(64), index=True, nullable=False, default='', comment='门店ID')
    channel_id = Column(String(64), index=True, nullable=False, default='', comment='渠道ID')
    channel_name = Column(String(64), nullable=False, default='', comment='渠道名称')
    status = Column(String(20), nullable=False, default='ONLINE', comment='状态:ONLINE-上架,OFFLINE-下架,NO_MID-无子商户,AUDIT-审核中,AUDIT_FAILED-审核失败')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')


class StoreChannelBase(BaseModel):
    store_id: str
    channel_id: str
    channel_name: str
    status: str = 'ONLINE'

class StoreChannelCreate(StoreChannelBase):
    pass

class StoreChannelUpdate(BaseModel):
    store_id: Optional[str] = None
    channel_id: Optional[str] = None    
    channel_name: Optional[str] = None
    status: Optional[str] = None
    
class StoreChannelResponse(StoreChannelBase):
    id: int
    create_time: datetime
    update_time: Optional[datetime] = None

    class Config:
        from_attributes = True