from dataclasses import dataclass


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
    ingredient_id: int
    quantity: float
    price: float
    entrance_date: str
    manufacture_date: str
    expire_date: str


@dataclass
class Part:
    id: int
    name: str
    ingredients: dict[int, float]  # list[dict[ingredient_id, float]


@dataclass
class Food:
    id: int
    name: str
    parts: list[int]  # list[part_id]


@dataclass
class EcoPack:
    id: int
    name: str
    foods: list[int]  # list[food_id]
    discount: float


@dataclass
class Order:
    id: int
    customer_id: int
    foods: list[int]  # list[food_id]
    price: float
    accept_time: str
    status: int  # 0 for pending and 1 for completed
    preparation_time: int  # Seconds


@dataclass
class Customer:
    id: int
    name: str
    last_name: str
