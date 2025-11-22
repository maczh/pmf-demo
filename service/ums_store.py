from models.ums_store import UmsStore, UmsStoreCreate, UmsStoreUpdate, UmsStoreResponse
from pmf.models import Result
from sqlalchemy.orm import Session
from common.vars import global_vars

db = global_vars.app.client.mysql.get_session()

def create_ums_store(store: UmsStoreCreate) -> Result:
    """创建ums_store"""
    try:
        db_ums_store = UmsStore(**store.dict())
        db.add(db_ums_store)
        db.commit()
        return Result.success(data=db_ums_store.to_dict())
    except Exception as e:
        return Result.error(msg=str(e))
    finally:
        db.close()


def delete_ums_store(id: int) -> Result:
    """删除ums_store"""
    try:
        db_ums_store = db.query(UmsStore).filter(UmsStore.id == id).first()
        if db_ums_store is None:
            return Result.error(msg="ums_store not found")
        db.delete(db_ums_store)
        db.commit()
        return Result.success()
    except Exception as e:
        return Result.error(msg=str(e))
    finally:
        db.close()


def update_ums_store(store: UmsStoreUpdate) -> Result:
    """更新ums_store"""
    try:
        db_ums_store = db.query(UmsStore).filter(UmsStore.id == store.id).first()
        if db_ums_store is None:
            return Result.error(msg="ums_store not found")
        for var, value in vars(store).items():
            if value is not None:
                setattr(db_ums_store, var, value)
        db.commit()
        return Result.success(data=db_ums_store.to_dict())
    except Exception as e:
        return Result.error(msg=str(e))
    finally:
        db.close()


def get_ums_store(id: int) -> Result:
    """获取ums_store"""
    try:
        db_ums_store = db.query(UmsStore).filter(UmsStore.id == id).first()
        if db_ums_store is None:
            return Result.error(msg="ums_store not found")
        return Result.success(data=db_ums_store.to_dict())
    except Exception as e:
        return Result.error(msg=str(e))
    finally:
        db.close()


def get_ums_store_by_store_id(store_id: str) -> Result:
    """通过store_id获取ums_store"""
    try:
        db_ums_store = db.query(UmsStore).filter(UmsStore.store_id == store_id).first()
        if db_ums_store is None:
            return Result.error(msg="ums_store not found")
        return Result.success(data=db_ums_store.to_dict())
    except Exception as e:
        return Result.error(msg=str(e))
    finally:
        db.close()


def list_ums_stores() -> Result:
    """获取ums_store列表"""
    try:
        db_ums_stores = db.query(UmsStore).all()
        data = [ums_store.to_dict() for ums_store in db_ums_stores]
        return Result.success(data=data)
    except Exception as e:
        return Result.error(msg=str(e))
    finally:
        db.close()
