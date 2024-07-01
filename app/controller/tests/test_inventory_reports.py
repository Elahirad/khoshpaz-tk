import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, Ingredient, IngredientInventoryItem
from app.view import IView


class TestInventoryReports(unittest.TestCase):

    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_critical_inventory_items(self):
        ingredients = [Ingredient(id=1, name='نمک', unit='گرم'), Ingredient(id=2, name='شکر', unit='کیلوگرم')]
        inventory_items = [
            IngredientInventoryItem(id=1, ingredient_id=1, quantity=5.0, price=10.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01'),
            IngredientInventoryItem(id=2, ingredient_id=2, quantity=15.0, price=20.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01')]
        self.data_storage.get_all.side_effect = [ingredients, inventory_items]
        result = self.controller.get_critical_inventory_items()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'نمک')
        self.assertEqual(result[0]['quantity'], 5.0)

    def test_get_most_valuable_inventory_items(self):
        ingredients = [Ingredient(id=1, name='نمک', unit='گرم'), Ingredient(id=2, name='شکر', unit='کیلوگرم')]
        inventory_items = [
            IngredientInventoryItem(id=1, ingredient_id=1, quantity=5.0, price=10.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01'),
            IngredientInventoryItem(id=2, ingredient_id=2, quantity=15.0, price=20.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01')]
        self.data_storage.get_all.side_effect = [ingredients, inventory_items]
        result = self.controller.get_most_valuable_inventory_items()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'شکر')
        self.assertEqual(result[0]['value'], 300.0)

    def test_get_expired_inventory_items(self):
        ingredients = [Ingredient(id=1, name='نمک', unit='گرم'), Ingredient(id=2, name='شکر', unit='کیلوگرم')]
        inventory_items = [
            IngredientInventoryItem(id=1, ingredient_id=1, quantity=5.0, price=10.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2022-01-01'),
            IngredientInventoryItem(id=2, ingredient_id=2, quantity=15.0, price=20.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2090-01-01')]
        self.data_storage.get_all.side_effect = [ingredients, inventory_items]
        result = self.controller.get_expired_inventory_items()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'نمک')
        self.assertEqual(result[0]['expire_date'], '2022-01-01')

    def test_get_duration_of_stay_in_inventory(self):
        ingredients = [Ingredient(id=1, name='نمک', unit='گرم'), Ingredient(id=2, name='شکر', unit='کیلوگرم')]
        inventory_items = [
            IngredientInventoryItem(id=1, ingredient_id=1, quantity=5.0, price=10.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01'),
            IngredientInventoryItem(id=2, ingredient_id=2, quantity=15.0, price=20.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01')]
        self.data_storage.get_all.side_effect = [ingredients, inventory_items]
        result = self.controller.get_duration_of_stay_in_inventory()
        self.assertEqual(len(result), 2)
        self.assertTrue(result[0]['duration'] >= 0)

    def test_get_count_inventory_items(self):
        ingredients = [Ingredient(id=1, name='نمک', unit='گرم'), Ingredient(id=2, name='شکر', unit='کیلوگرم')]
        inventory_items = [
            IngredientInventoryItem(id=1, ingredient_id=1, quantity=5.0, price=10.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01'),
            IngredientInventoryItem(id=2, ingredient_id=2, quantity=15.0, price=20.0, entrance_date='2023-01-01',
                                    manufacture_date='2023-01-01', expire_date='2024-01-01')]
        self.data_storage.get_all.side_effect = [ingredients, inventory_items]
        result = self.controller.get_count_inventory_items()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['quantity'], 5.0)
        self.assertEqual(result[1]['quantity'], 15.0)
