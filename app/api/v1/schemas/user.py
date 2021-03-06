from datetime import datetime
from enum import Enum
from uuid import UUID

from bson import ObjectId

from app.api.v1.schemas.base import BaseEnhancedModel


class EGender(str, Enum):
    male = "male"
    female = "female"


class UserBase(BaseEnhancedModel):
    fullname: str
    username: str
    email: str
    phone: str
    date_of_birth: datetime
    bio: str
    gender: EGender


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserSchema(UserBase):
    id: int


class UserMongoSchema(UserBase):
    _id: ObjectId
    object_id: UUID
