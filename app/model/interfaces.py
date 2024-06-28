from abc import ABC, abstractmethod
from app.model.dataclasses import *


class IAdminStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_admins() -> list[Admin]: pass

    @staticmethod
    @abstractmethod
    def get_admin(admin_id: int) -> Admin: pass

    @staticmethod
    @abstractmethod
    def add_admin(admin: Admin) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_admin(admin_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_admin(admin: Admin) -> None: pass


class IIngredientStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_ingredients() -> list[Ingredient]: pass

    @staticmethod
    @abstractmethod
    def get_ingredient(ingredient_id: int) -> Ingredient: pass

    @staticmethod
    @abstractmethod
    def add_ingredient(ingredient: Ingredient) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_ingredient(ingredient_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_ingredient(ingredient: Ingredient) -> None: pass


class IIngredientInventoryItemStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_inventory_item() -> IngredientInventoryItem: pass

    @staticmethod
    @abstractmethod
    def add_inventory_item(item: IngredientInventoryItem) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_inventory_item(item_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_inventory_item(item: IngredientInventoryItem) -> None: pass


class IPartStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_parts() -> list[Part]: pass

    @staticmethod
    @abstractmethod
    def get_part(part_id: int) -> Part: pass

    @staticmethod
    @abstractmethod
    def add_part(part: Part) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_part(part_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_part(part: Part) -> None: pass


class IFoodStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_foods() -> list[Food]: pass

    @staticmethod
    @abstractmethod
    def get_food(food_id: int) -> Food: pass

    @staticmethod
    @abstractmethod
    def add_food(food: Food) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_food(food_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_food(food: Food) -> None: pass


class IEcoPackStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_eco_packs() -> list[EcoPack]: pass

    @staticmethod
    @abstractmethod
    def get_eco_pack(eco_pack_id: int) -> EcoPack: pass

    @staticmethod
    @abstractmethod
    def add_eco_pack(eco_pack: EcoPack) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_eco_pack(eco_pack_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_eco_pack(eco_pack: EcoPack) -> None: pass


class IOrderStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_orders() -> list[Order]: pass

    @staticmethod
    @abstractmethod
    def get_order(order_id: int) -> Order: pass

    @staticmethod
    @abstractmethod
    def add_order(order: Order) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_order(order_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_order(order: Order) -> None: pass


class ICustomerStorage(ABC):
    @staticmethod
    @abstractmethod
    def get_customers() -> list[Customer]: pass

    @staticmethod
    @abstractmethod
    def get_customer(customer_id: int) -> Customer: pass

    @staticmethod
    @abstractmethod
    def add_customer(customer: Customer) -> None: pass

    @staticmethod
    @abstractmethod
    def remove_customer(customer_id: int) -> None: pass

    @staticmethod
    @abstractmethod
    def update_customer(customer: Customer) -> None: pass
