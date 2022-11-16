from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.postgres.base_models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id_in: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id_in).first()

    def get_multi(
            self, db: Session, page_no: int = 1, page_size: int = 10,
            condition_in: dict = None, order_by: str = None
    ) -> List[ModelType]:
        db_query = db.query(self.model)
        if condition_in:
            for db_field, field_val in condition_in.items():
                db_query = db_query.filter(getattr(self.model, db_field) == field_val)
        if order_by:
            db_query.order_by(getattr(self.model, order_by))
        end = page_no * page_size
        db_query = db_query.offset(end - page_size).limit(end)

        return db_query.all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def query_update(self, db: Session, condition_in: dict, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data: dict = jsonable_encoder(obj_in)
        db_qu = db.query(self.model)
        if condition_in:
            for db_field, field_val in condition_in.items():
                db_qu = db_qu.filter(getattr(self.model, db_field) == field_val)
        result = db_qu.update(obj_in_data)
        db.commit()
        return result

    @staticmethod
    def update(
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id_in: int) -> ModelType:
        obj = db.query(self.model).get(id_in)
        db.delete(obj)
        db.commit()
        return obj
