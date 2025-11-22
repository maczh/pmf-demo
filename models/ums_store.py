from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

Base = declarative_base()

class UmsStore(Base):
    __tablename__ = 'ums_store_geo'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='主键ID')
    store_id = Column(String(64), nullable=False, default='', comment='门店ID')
    latitude = Column(String(12), nullable=False, default='', comment='纬度')
    longitude = Column(String(12), nullable=False, default='', comment='经度')

    def to_dict(self):
        return {
            'id': self.id,
            'store_id': self.store_id,
            'latitude': self.latitude,
            'longitude': self.longitude
        }


class UmsStoreBase(BaseModel):
    id: int
    store_id: str
    latitude: str
    longitude: str

class UmsStoreCreate(UmsStoreBase):
    pass

class UmsStoreUpdate(BaseModel):
    id: int
    store_id: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None

class UmsStoreResponse(UmsStoreBase):
    pass
    class Config:
        from_attributes = True

    