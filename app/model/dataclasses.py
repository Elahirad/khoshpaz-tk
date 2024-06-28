from dataclasses import dataclass
from datetime import datetime


@dataclass
class Admin:
    id: int
    username: str
    password: str


@dataclass
class Ingredient:
    id: int
    name: str
    unit: str


@dataclass
class IngredientInventoryItem:
    id: int
    ingredient: Ingredient
    quantity: float
    price: float
    entrance_date: datetime
    manufacture_date: datetime
    expire_date: datetime


@dataclass
class Part:
    id: int
    name: str
    ingredients: list[dict[Ingredient, float]]


@dataclass
class Food:
    id: int
    name: str
    parts: list[Part]


@dataclass
class EcoPack:
    id: int
    name: str
    foods: list[Food]
    discount: float


@dataclass
class Order:
    id: int
    customer_id: int
    foods: list[Food]
    price: float
    accept_time: datetime
    status: int  # 0 for pending and 1 for completed
    preparation_time: int  # Seconds


@dataclass
class Customer:
    id: int
    name: str
    orders: list[Order]
