from sqlalchemy import Boolean, Column, Integer, String, text
from sqlalchemy.dialects.postgresql import TIMESTAMP

from db.postgres.base_models import Base, ReprMixin


class AppAuthentication(Base, ReprMixin):
    __tablename__ = 'app_authentication'

    app_authentication_id = Column(Integer, primary_key=True)
    type = Column(String(100), comment='APP authentication type: sms, code')
    platform = Column(String)
    token = Column(String)
    is_enabled = Column(Boolean, server_default=text("true"))
    create_time = Column(TIMESTAMP(True, 3), server_default=text("now()"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("now()"))
    create_by = Column(String(100))
    modify_by = Column(String(100))
