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
    ingredients: dict[int, float]  # dict[ingredient_id, float]


@dataclass
class Food:
    id: int
    name: str
    price: float
    parts: dict[int, int]  # dict[part_id, amount]


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
    foods: dict[int, int]  # dict[food_id, amount]
    paid_amount: float
    accept_time: str
    status: int  # 0 for pending and 1 for completed
    preparation_time: float  # Hours


@dataclass
class Customer:
    id: int
    name: str
    last_name: str
