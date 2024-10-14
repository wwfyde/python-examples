from datetime import datetime

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None
    friends: list[int] = []
    addresses: list["Address"] = []


if __name__ == '__main__':
    user = User.model_validate({'id': 13, 'name': "Kayn Asa", 'signup_ts': datetime.now()})
    user = user.model_copy(
        update={'friends': [1, 2, 3], 'addresses': [Address(**{'street': '123', 'city': 'Shanghai'})]})
    print(type(user.addresses[0]))
    print(type(user))
