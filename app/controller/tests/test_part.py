import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, Part, Ingredient
from app.view import IView


class TestPart(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_parts(self):
        part = Part(id=1, name='جزء اول', ingredients={1: 100})
        ingredient = Ingredient(id=1, name='نمک', unit='گرم')
        self.data_storage.get_all.side_effect = [[part], [ingredient]]
        self.data_storage.get.return_value = ingredient
        parts = self.controller.get_parts()
        self.assertEqual(len(parts), 1)
        self.assertIn('نمک', parts[0]['ingredients'][0])

    def test_add_part(self):
        part = Part(id=1, name='جزء اول', ingredients={1: 100})
        self.data_storage.add.return_value = part
        result = self.controller.add_part('جزء اول', {1: 100})
        self.assertEqual(result['name'], 'جزء اول')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['parts'])

    def test_update_part(self):
        part = Part(id=1, name='جزء اول', ingredients={1: 100})
        self.data_storage.get.return_value = part
        self.data_storage.update.return_value = part
        result = self.controller.update_part(1, 'جزء اول آپدیت شده', {2: 200})
        self.assertEqual(result['name'], 'جزء اول آپدیت شده')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['parts'])

    def test_remove_part(self):
        part = Part(id=1, name='جزء اول', ingredients={1: 100})
        self.data_storage.get.return_value = part
        self.data_storage.get_all.return_value = []
        result = self.controller.remove_part(1)
        self.assertTrue(result)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['parts'])
