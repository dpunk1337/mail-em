from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from backend.models import *


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User


class Mail(SQLAlchemyAutoSchema):
    class Meta:
        model = Mail

class UserMailMap(SQLAlchemyAutoSchema):
    class Meta:
        model = UserMailMap
