import datetime

from app.view.interface import IView
from app.model import IDataStorage
from app.model import Ingredient, Part, Food, Customer, Order, IngredientInventoryItem


class Controller:
    def __init__(self, view: IView, data_storage: IDataStorage) -> None:
        self._view = view
        self._view.controller = self
        self._data_storage = data_storage
        self._view.reload_app_data()

    # --------------------- Ingredients ---------------------#
    def get_ingredients(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            return self._data_storage.get(Ingredient, item_id).__dict__
        return list(map(lambda o: o.__dict__, self._data_storage.get_all(Ingredient)))

    def add_ingredient(self, name: str, unit: str) -> dict:
        ing = Ingredient(1, name, unit)
        ing = self._data_storage.add(ing).__dict__
        self._view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self._view.reload_app_data()
        return ing

    def update_ingredient(self, item_id: int, name: str, unit: str) -> dict:
        ingredient = self._data_storage.get(Ingredient, item_id)
        if ingredient:
            ingredient.name = name
            ingredient.unit = unit
            ingredient = self._data_storage.update(ingredient)
            self._view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self._view.reload_app_data()
            return ingredient.__dict__
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_ingredient(self, item_id: int) -> bool:
        ing = self._data_storage.get(Ingredient, item_id)
        parts = self._data_storage.get_all(Part)
        if ing:
            for part in parts:
                for ingredient_id, amount in part.ingredients.items():
                    if ingredient_id == ing.id:
                        self._view.show_message('خطا',
                                                'امکان حذف کردن این ماده وجود ندارد. زیرا در اجزاء غذاها، جزئی با این ماده وجود دارد',
                                                'cancel')
                        return False
            self._data_storage.remove(Ingredient, item_id)
            self._view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self._view.reload_app_data()
            return True
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    # -------------------------------------------------------#

    # ------------------------ Parts ------------------------#
    def get_parts(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            part = self._data_storage.get(Part, item_id).__dict__
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
        parts = list(map(lambda o: o.__dict__, self._data_storage.get_all(Part)))
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
        part = self._data_storage.add(part).__dict__
        self._view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self._view.reload_app_data()
        return part

    def update_part(self, item_id: int, name: str, ingredients: dict[int, float]) -> dict:
        part = self._data_storage.get(Part, item_id)
        if part:
            part.name = name
            part.ingredients = ingredients
            part = self._data_storage.update(part)
            self._view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self._view.reload_app_data()
            return part.__dict__
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_part(self, item_id: int) -> bool:
        part = self._data_storage.get(Part, item_id)
        foods = self._data_storage.get_all(Food)
        if part:
            for food in foods:
                for part_id, amount in food.parts.items():
                    if part.id == part_id:
                        self._view.show_message('خطا',
                                                'امکان حذف کردن این جزء وجود ندارد. زیرا غذایی با این جزء وجود دارد',
                                                'cancel')
                        return False

            self._data_storage.remove(Part, item_id)
            self._view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self._view.reload_app_data()
            return True
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    # -------------------------------------------------------#

    # ---------------------- Customers ----------------------#
    def get_customers(self, customer_id: int = None) -> list[dict] | dict:
        if customer_id:
            customer = self._data_storage.get(Customer, customer_id)
            if customer:
                return customer.__dict__
            self._view.show_message("خطا", "مشتری مورد نظر یافت نشد", icon="cancel")
        return list(map(lambda o: o.__dict__, self._data_storage.get_all(Customer)))

    def add_customer(self, name: str, last_name: str) -> dict:
        customer = Customer(1, name, last_name)
        customer = self._data_storage.add(customer).__dict__
        self._view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self._view.reload_app_data()
        return customer

    def update_customer(self, customer_id: int, name: str, last_name: str) -> dict:
        customer = self._data_storage.get(Customer, customer_id)
        if customer:
            customer.name = name
            customer.last_name = last_name
            customer = self._data_storage.update(customer)
            self._view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self._view.reload_app_data()
            return customer.__dict__
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_customer(self, customer_id: int) -> bool:
        customer = self._data_storage.get(Customer, customer_id)
        orders = self._data_storage.get_all(Order)
        if customer:
            for order in orders:
                if order.customer_id == customer.id:
                    self._view.show_message('خطا',
                                            'امکان حذف کردن این مشتری وجود ندارد. زیرا سفارش‌هایی برای این مشتری وجود دارد',
                                            'cancel')
                    return False
            self._data_storage.remove(Customer, customer_id)
            self._view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self._view.reload_app_data()
            return True
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    # -------------------------------------------------------#

    # ------------------------ Foods ------------------------#
    def get_foods(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            food = self._data_storage.get(Food, item_id).__dict__
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
        foods = list(map(lambda o: o.__dict__, self._data_storage.get_all(Food)))
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
        food = self._data_storage.add(food).__dict__
        self._view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self._view.reload_app_data()
        return food

    def update_food(self, item_id: int, name: str, price: float, parts: dict[int, int]) -> dict:

        food = self._data_storage.get(Food, item_id)
        if food:
            food.name = name
            food.price = price
            food.parts = parts
            food = self._data_storage.update(food)
            self._view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self._view.reload_app_data()
            return food.__dict__
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_food(self, item_id: int) -> bool:
        food = self._data_storage.get(Food, item_id)
        orders = self._data_storage.get_all(Order)
        if food:
            for order in orders:
                for food_id, amount in order.foods.items():
                    if food_id == food.id:
                        self._view.show_message('خطا',
                                                'امکان حذف کردن این غذا وجود ندارد. زیرا سفارش‌هایی با این غذا وجود دارد',
                                                'cancel')
                        return False
            self._data_storage.remove(Food, item_id)
            self._view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self._view.reload_app_data()
            return True
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    # -------------------------------------------------------#

    # ------------------------ Orders -----------------------#
    def get_orders(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            order = self._data_storage.get(Order, item_id).__dict__
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
        orders = list(map(lambda o: o.__dict__, self._data_storage.get_all(Order)))
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

    def add_order(self, customer_id: int, foods: dict[int, int], paid_amount: float, accept_time: str, status: int,
                  preparation_time: float) -> dict:
        order = Order(1, customer_id, foods, paid_amount, accept_time, status, preparation_time)
        order = self._data_storage.add(order).__dict__
        self._view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self._view.reload_app_data()
        return order

    def update_order(self, item_id: int, customer_id: int, foods: dict[int, int], paid_amount: float, accept_time: str,
                     status: int,
                     preparation_time: float) -> dict:

        order = self._data_storage.get(Order, item_id)
        if order:
            order.customer_id = customer_id
            order.paid_amount = paid_amount
            order.accept_time = accept_time
            order.status = status
            order.preparation_time = preparation_time
            order.foods = foods
            order = self._data_storage.update(order)
            self._view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self._view.reload_app_data()
            return order.__dict__
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_order(self, item_id: int) -> bool:
        order = self._data_storage.get(Order, item_id)
        if order:
            self._data_storage.remove(Order, item_id)
            self._view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self._view.reload_app_data()
            return True
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    # -------------------------------------------------------#

    # ------------------- Inventory Items -------------------#
    def get_inventory_items(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            inventory_item = self._data_storage.get(IngredientInventoryItem, item_id).__dict__
            ingredient_id = inventory_item['ingredient_id']
            ingredient = self.get_ingredients(int(ingredient_id))
            inventory_item['ingredient'] = ingredient['name']
            return inventory_item
        inventory_items = list(map(lambda o: o.__dict__, self._data_storage.get_all(IngredientInventoryItem)))
        for inventory_item in inventory_items:
            ingredient_id = inventory_item['ingredient_id']
            ingredient = self.get_ingredients(int(ingredient_id))
            inventory_item['ingredient'] = ingredient['name']
        return inventory_items

    def add_inventory_item(self, ingredient_id: int, quantity: float, price: float, entrance_data: str,
                           manufacture_date: str, expire_data: str) -> dict:
        inventory_item = IngredientInventoryItem(1, ingredient_id, quantity, price, entrance_data,
                                                 manufacture_date, expire_data)
        inventory_item = self._data_storage.add(inventory_item).__dict__
        self._view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self._view.reload_app_data()
        return inventory_item

    def update_inventory_item(self, item_id: int, ingredient_id: int, quantity: float, price: float, entrance_date: str,
                              manufacture_date: str, expire_date: str) -> dict:

        inventory_item = self._data_storage.get(IngredientInventoryItem, item_id)
        if inventory_item:
            inventory_item.ingredient_id = ingredient_id
            inventory_item.quantity = quantity
            inventory_item.price = price
            inventory_item.entrance_date = entrance_date
            inventory_item.manufacture_date = manufacture_date
            inventory_item.expire_date = expire_date
            inventory_item = self._data_storage.update(inventory_item)
            self._view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self._view.reload_app_data()
            return inventory_item.__dict__
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_inventory_item(self, item_id: int) -> bool:
        inventory_item = self._data_storage.get(IngredientInventoryItem, item_id)
        if inventory_item:
            self._data_storage.remove(IngredientInventoryItem, item_id)
            self._view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self._view.reload_app_data()
            return True
        else:
            self._view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    def get_critical_inventory_items(self) -> list[dict]:
        result = {}
        ingredients = self._data_storage.get_all(Ingredient)
        in_stock = {ing.id: 0 for ing in ingredients}
        items = self._data_storage.get_all(IngredientInventoryItem)
        for item in items:
            in_stock[item.ingredient_id] += item.quantity
        for ing, count in in_stock.items():
            if count < 10:
                result[ingredients[next(
                    i for i, v in enumerate(ingredients) if v.id == ing)].name] = 'ناموجود' if count == 0 else count
        return [{'name': k, 'quantity': v} for k, v in
                result.items()]

    def get_most_valuable_inventory_items(self) -> list:
        result = []
        ingredients = self._data_storage.get_all(Ingredient)
        values = {ing.id: 0 for ing in ingredients}
        items = self._data_storage.get_all(IngredientInventoryItem)
        for item in items:
            values[item.ingredient_id] += item.quantity * item.price
        for ing, value in values.items():
            result.append((ingredients[next(
                i for i, v in enumerate(ingredients) if v.id == ing)].name, value))

        result = list(sorted(result, key=lambda x: x[1], reverse=True))
        return [{'name': v[0], 'value': v[1]} for v in
                result]

    def get_expired_inventory_items(self) -> list[dict]:
        result = {}
        ingredients = self._data_storage.get_all(Ingredient)
        items = self._data_storage.get_all(IngredientInventoryItem)
        for item in items:
            if datetime.datetime.strptime(item.expire_date, '%Y-%m-%d') < datetime.datetime.now():
                result[ingredients[
                    next(i for i, v in enumerate(ingredients) if v.id == item.ingredient_id)].name] = (
                    item.id, item.expire_date)
        return [{'id': v[0], 'name': k, 'expire_date': v[1]} for k, v in
                result.items()]

    def get_duration_of_stay_in_inventory(self) -> list[dict]:
        result = {}
        ingredients = self._data_storage.get_all(Ingredient)
        items = self._data_storage.get_all(IngredientInventoryItem)
        for item in items:
            timedelta = (datetime.datetime.now() - datetime.datetime.strptime(item.entrance_date, '%Y-%m-%d'))
            result[ingredients[
                next(
                    i for i, v in enumerate(ingredients) if v.id == item.ingredient_id)].name] = (
                item.id, timedelta.days)
        return [{'id': v[0], 'name': k, 'duration': v[1]} for k, v in
                result.items()]

    def get_count_inventory_items(self) -> list[dict]:
        result = {}
        ingredients = self._data_storage.get_all(Ingredient)
        in_stock = {ing.id: 0 for ing in ingredients}
        items = self._data_storage.get_all(IngredientInventoryItem)
        for item in items:
            in_stock[item.ingredient_id] += item.quantity
        for ing, count in in_stock.items():
            result[ingredients[next(
                i for i, v in enumerate(ingredients) if v.id == ing)].name] = count
        return [{'name': k, 'quantity': v} for k, v in
                result.items()]
    # -------------------------------------------------------#
