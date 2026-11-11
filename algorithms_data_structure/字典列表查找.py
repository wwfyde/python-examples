from typing import TypedDict

from pydantic import BaseModel, TypeAdapter


class Fruit(TypedDict):
    name: str
    color: str
    weight: float
    price: float
    quantity: int
    is_ripe: bool
    is_organic: bool
    origin: str
    harvest_date: str
    expiration_date: str


type FruitList = list[Fruit]
fruits: FruitList = [
    Fruit(
        name="苹果",
        color="红色",
        weight=0.2,
        price=3.5,
        quantity=10,
        is_ripe=True,
        is_organic=False,
        origin="中国",
        harvest_date="2023-09-01",
        expiration_date="2023-09-15",
    ),
    Fruit(
        name="香蕉",
        color="黄色",
        weight=0.15,
        price=2.0,
        quantity=20,
        is_ripe=True,
        is_organic=True,
        origin="菲律宾",
        harvest_date="2023-09-05",
        expiration_date="2023-09-20",
    ),
]


class FruitPydantic(BaseModel):
    name: str
    color: str
    weight: float
    price: float
    quantity: int
    is_ripe: bool
    is_organic: bool
    origin: str
    harvest_date: str
    expiration_date: str


apple: Fruit | None = next((item for item in fruits if item["name"] == "苹果"), None)


def find_fruit(name: str) -> Fruit | None:
    """
    查找水果
    :param name: 水果名称
    :return: 水果信息
    """
    return next((item for item in fruits if item["name"] == name), None)


print(apple)

print(find_fruit("香蕉"))

fruit_pd = TypeAdapter(Fruit)
print(fruit_pd.validate_python(apple))
print(fruit_pd.pydantic_complete)

apple_pydantic = FruitPydantic.model_validate(apple)
print(apple_pydantic)
