from pydantic import BaseModel, Field
from datetime import date


class User(BaseModel):
    id: int
    name: str
    dob: date = Field(title='Date of Birth')


# define some users
users = [
    User(id=1, name='John', dob=date(1990, 1, 1)),
    User(id=2, name='Jack', dob=date(1991, 1, 1)),
    User(id=3, name='Jill', dob=date(1992, 1, 1)),
    User(id=4, name='Jane', dob=date(1993, 1, 1)),
]
