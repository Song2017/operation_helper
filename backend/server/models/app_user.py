# coding: utf-8
from sqlalchemy import Boolean, Column, Integer, String, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

from db.postgres.base_models import ReprMixin

Base = declarative_base()
metadata = Base.metadata


class AppUser(Base, ReprMixin):
    __tablename__ = 'app_user'

    app_user_id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    email = Column(String(100))
    hashed_password = Column(String)
    is_active = Column(Boolean, server_default=text("true"))
    is_superuser = Column(Boolean, server_default=text("false"))

    create_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    create_by = Column(String(100))
    modify_by = Column(String(100))
