from sqlalchemy import Boolean, Column, Integer, String, text
from sqlalchemy.dialects.postgresql import TIMESTAMP

from db.postgres.base_models import Base, ReprMixin


class AppOperationInfo(Base, ReprMixin):
    __tablename__ = 'app_operation_info'

    app_operation_info_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(100))
    content = Column(String)
    is_consumed = Column(Boolean, server_default=text("true"))
    create_time = Column(TIMESTAMP(True, 3), server_default=text("now()"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("now()"))
    create_by = Column(String(100))
    modify_by = Column(String(100))
