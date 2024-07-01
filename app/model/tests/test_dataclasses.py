import unittest
from app.model.types import *


class TestDataClassesCreation(unittest.TestCase):

    def test_ingredient_creation(self):
        ingredient = Ingredient(id=1, name="Ab", unit='kg')
        self.assertEqual(ingredient.id, 1)
        self.assertEqual(ingredient.name, "Ab")
        self.assertEqual(ingredient.unit, "kg")

    def test_ingredient_inventory_item_creation(self):
        ingredient_inventory_item = IngredientInventoryItem(id=1, ingredient_id=1, quantity=34, price=123456,
                                                            expire_date='1999-01-01', manufacture_date='1999-02-02',
                                                            entrance_date='1999-03-03')
        self.assertEqual(ingredient_inventory_item.id, 1)
        self.assertEqual(ingredient_inventory_item.ingredient_id, 1)
        self.assertEqual(ingredient_inventory_item.quantity, 34)
        self.assertEqual(ingredient_inventory_item.price, 123456)
        self.assertEqual(ingredient_inventory_item.expire_date, '1999-01-01')
        self.assertEqual(ingredient_inventory_item.manufacture_date, '1999-02-02')
        self.assertEqual(ingredient_inventory_item.entrance_date, '1999-03-03')

    def test_part_creation(self):
        part = Part(id=1, name="AbcDef", ingredients={1: 0.3, 2: 0.5, 3: 0.6}, )
        self.assertEqual(part.id, 1)
        self.assertEqual(part.name, "AbcDef")
        self.assertEqual(part.ingredients, {1: 0.3, 2: 0.5, 3: 0.6})

    def test_customer_creation(self):
        customer = Customer(id=1, name="Ali", last_name="Elahirad")
        self.assertEqual(customer.id, 1)
        self.assertEqual(customer.name, "Ali")
        self.assertEqual(customer.last_name, "Elahirad")

    def test_order_creation(self):
        order = Order(id=1, customer_id=1, foods={1: 1, 2: 0.5}, paid_amount=123456, preparation_time=2,
                      accept_time='2000-01-01', status=0)
        self.assertEqual(order.id, 1)
        self.assertEqual(order.customer_id, 1)
        self.assertEqual(order.foods, {1: 1, 2: 0.5})
        self.assertEqual(order.paid_amount, 123456)
        self.assertEqual(order.preparation_time, 2)
        self.assertEqual(order.accept_time, '2000-01-01')
        self.assertEqual(order.status, 0)

    def test_food_creation(self):
        food = Food(id=1, name="پیتزا", price=12.99, parts={1: 2, 2: 3})
        self.assertEqual(food.id, 1)
        self.assertEqual(food.name, "پیتزا")
        self.assertEqual(food.price, 12.99)
        self.assertEqual(food.parts, {1: 2, 2: 3})
