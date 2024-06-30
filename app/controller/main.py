from app.view.interface import IView
from app.model import IDataStorage
from app.model import Ingredient, Part, Food, Customer, Order


class Controller:
    def __init__(self, view: IView, data_storage: IDataStorage) -> None:
        self.view = view
        self.view.controller = self
        self.data_storage = data_storage
        self.view.reload_app_data()

    def get_ingredients(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            return self.data_storage.get(Ingredient, item_id).__dict__
        return list(map(lambda o: o.__dict__, self.data_storage.get_all(Ingredient)))

    def add_ingredient(self, name: str, unit: str) -> dict:
        ing = Ingredient(1, name, unit)
        ing = self.data_storage.add(ing).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self.view.reload_app_data()
        return ing

    def update_ingredient(self, item_id: int, name: str, unit: str) -> dict:
        ingredient = self.data_storage.get(Ingredient, item_id)
        if ingredient:
            ingredient.name = name
            ingredient.unit = unit
            ingredient = self.data_storage.update(ingredient)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self.view.reload_app_data()
            return ingredient.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_ingredient(self, item_id: int) -> bool:
        ing = self.data_storage.get(Ingredient, item_id)
        if ing:
            self.data_storage.remove(Ingredient, item_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self.view.reload_app_data()
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    def get_parts(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            part = self.data_storage.get(Part, item_id).__dict__
            ingredients = part['ingredients']
            ingredients_raw = {}
            new_ingredients = []
            for ing_id, amount in ingredients.items():
                ingredient = self.get_ingredients(int(ing_id))
                ingredients_raw[ingredient['name']] = amount
                new_ingredients.append(f"{ingredient['name']}: {amount} {ingredient['unit']}")
            part['ingredients'] = new_ingredients
            part['ingredients_raw'] = ingredients_raw
            return part
        parts = list(map(lambda o: o.__dict__, self.data_storage.get_all(Part)))
        for idx, part in enumerate(parts):
            ingredients = part['ingredients']
            ingredients_raw = {}
            new_ingredients = []
            for ing_id, amount in ingredients.items():
                ingredient = self.get_ingredients(int(ing_id))
                ingredients_raw[ingredient['name']] = amount
                new_ingredients.append(f"{ingredient['name']}: {amount} {ingredient['unit']}")
            part['ingredients'] = new_ingredients
            part['ingredients_raw'] = ingredients_raw
        return parts

    def add_part(self, name: str, ingredients: dict[int, float]):
        part = Part(1, name, ingredients)
        part = self.data_storage.add(part).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self.view.reload_app_data()
        return part

    def update_part(self, item_id: int, name: str, ingredients: dict[int, float]) -> dict:
        part = self.data_storage.get(Part, item_id)
        if part:
            part.name = name
            part.ingredients = ingredients
            part = self.data_storage.update(part)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self.view.reload_app_data()
            return part.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_part(self, item_id: int) -> bool:
        part = self.data_storage.get(Part, item_id)
        if part:
            self.data_storage.remove(Part, item_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self.view.reload_app_data()
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    def get_customers(self, customer_id: int = None) -> list[dict] | dict:
        if customer_id:
            customer = self.data_storage.get(Customer, customer_id)
            if customer:
                return customer.__dict__
            self.view.show_message("خطا", "مشتری مورد نظر یافت نشد", icon="cancel")
        return list(map(lambda o: o.__dict__, self.data_storage.get_all(Customer)))

    def add_customer(self, name: str, last_name: str) -> dict:
        customer = Customer(1, name, last_name)
        customer = self.data_storage.add(customer).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self.view.reload_app_data()
        return customer

    def update_customer(self, customer_id: int, name: str, last_name: str) -> dict:
        customer = self.data_storage.get(Customer, customer_id)
        if customer:
            customer.name = name
            customer.last_name = last_name
            customer = self.data_storage.update(customer)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self.view.reload_app_data()
            return customer.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_customer(self, customer_id: int) -> bool:
        customer = self.data_storage.get(Customer, customer_id)
        if customer:
            self.data_storage.remove(Customer, customer_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self.view.reload_app_data()
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    def get_foods(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            food = self.data_storage.get(Food, item_id).__dict__
            parts = food['parts']
            parts_raw = {}
            new_parts = []
            for ing_id, amount in parts.items():
                part = self.get_parts(int(ing_id))
                parts_raw[part['name']] = amount
                new_parts.append(f"{part['name']}: {amount}")
            food['parts'] = new_parts
            food['parts_raw'] = parts_raw
            return food
        foods = list(map(lambda o: o.__dict__, self.data_storage.get_all(Food)))
        for idx, food in enumerate(foods):
            parts = food['parts']
            parts_raw = {}
            new_parts = []
            for part_id, amount in parts.items():
                part = self.get_parts(int(part_id))
                parts_raw[part['name']] = amount
                new_parts.append(f"{part['name']}: {amount}")
            food['parts'] = new_parts
            food['parts_raw'] = parts_raw
        return foods

    def add_food(self, name: str, price: float, parts: dict[int, int]):
        food = Food(1, name, price, parts)
        food = self.data_storage.add(food).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self.view.reload_app_data()
        return food

    def update_food(self, item_id: int, name: str, price: float, parts: dict[int, int]) -> dict:

        food = self.data_storage.get(Food, item_id)
        if food:
            food.name = name
            food.price = price
            food.parts = parts
            food = self.data_storage.update(food)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self.view.reload_app_data()
            return food.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_food(self, item_id: int) -> bool:
        food = self.data_storage.get(Food, item_id)
        if food:
            self.data_storage.remove(Food, item_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self.view.reload_app_data()
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    def get_orders(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            order = self.data_storage.get(Order, item_id).__dict__
            foods = order['foods']
            foods_raw = {}
            new_foods = []
            for ing_id, amount in foods.items():
                food = self.get_foods(int(ing_id))
                foods_raw[food['name']] = amount
                new_foods.append(f"{food['name']}: {amount}")
            order['foods'] = new_foods
            order['foods_raw'] = foods_raw
            customer = self.get_customers(int(order['customer_id']))
            order['customer'] = f"{customer['name']}: {customer['last_name']}"
            order['status_raw'] = order['status']
            order['status'] = 'تکمیل شده' if order['status'] else 'در حال آماده سازی'
            return order
        orders = list(map(lambda o: o.__dict__, self.data_storage.get_all(Order)))
        for idx, order in enumerate(orders):
            foods = order['foods']
            foods_raw = {}
            new_foods = []
            for food_id, amount in foods.items():
                food = self.get_foods(int(food_id))
                foods_raw[food['name']] = amount
                new_foods.append(f"{food['name']}: {amount}")
            order['foods'] = new_foods
            order['foods_raw'] = foods_raw
            customer = self.get_customers(int(order['customer_id']))
            order['customer'] = f"{customer['name']} {customer['last_name']}"
            order['status_raw'] = order['status']
            order['status'] = 'تکمیل شده' if order['status'] else 'در حال آماده سازی'
        return orders

    def add_order(self, customer_id: int, foods: dict[int, int], paid_amout: float, accept_time: str, status: int,
                  preparation_time: float) -> dict:
        order = Order(1, customer_id, foods, paid_amout, accept_time, status, preparation_time)
        order = self.data_storage.add(order).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self.view.reload_app_data()
        return order

    def update_order(self, item_id: int, customer_id: int, foods: dict[int, int], paid_amout: float, accept_time: str,
                     status: int,
                     preparation_time: float) -> dict:

        order = self.data_storage.get(Order, item_id)
        if order:
            order.customer_id = customer_id
            order.paid_amount = paid_amout
            order.accept_time = accept_time
            order.status = status
            order.preparation_time = preparation_time
            order.foods = foods
            order = self.data_storage.update(order)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self.view.reload_app_data()
            return order.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_order(self, item_id: int) -> bool:
        order = self.data_storage.get(Order, item_id)
        if order:
            self.data_storage.remove(Order, item_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self.view.reload_app_data()
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False
