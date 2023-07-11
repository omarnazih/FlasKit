from pony.orm import *
from pydantic import BaseModel, Field

from app import db

import uuid


class Todo(db.Entity):
    _id = Required(str, unique=True, default=lambda: str(uuid.uuid4()))
    title = Required(str)
    description = Required(str)
    completed = Required(bool, default=False)