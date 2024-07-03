import unittest
from dataclasses import dataclass
from unittest.mock import mock_open, patch

from app.model.datastorage.json_storage import JSONStorage


@dataclass
class TestModel:
    __test__ = False
    id: int
    name: str
    value: int


class TestJSONStorage(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_get_all_empty(self, mock_file):
        storage = JSONStorage('test_data.json')
        items = storage.get_all(TestModel)
        self.assertEqual(items, [])

    @patch('builtins.open', new_callable=mock_open, read_data='{"TestModel": [{"id": 1, "name": "test", "value": 10}]}')
    def test_get_all_with_data(self, mock_file):
        storage = JSONStorage('test_data.json')
        items = storage.get_all(TestModel)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].id, 1)
        self.assertEqual(items[0].name, 'test')
        self.assertEqual(items[0].value, 10)

    @patch('builtins.open', new_callable=mock_open, read_data='{"TestModel": [{"id": 1, "name": "test", "value": 10}]}')
    def test_get_existing_item(self, mock_file):
        storage = JSONStorage('test_data.json')
        item = storage.get(TestModel, 1)
        self.assertIsNotNone(item)
        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, 'test')
        self.assertEqual(item.value, 10)

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_get_non_existing_item(self, mock_file):
        storage = JSONStorage('test_data.json')
        item = storage.get(TestModel, 1)
        self.assertIsNone(item)

    @patch('app.model.datastorage.json_storage.JSONStorage._save')
    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_add_item(self, mock_file, mock_save):
        storage = JSONStorage('test_data.json')
        new_item = TestModel(id=0, name='new', value=100)
        added_item = storage.add(new_item)
        self.assertEqual(added_item.id, 1)
        self.assertEqual(added_item.name, 'new')
        self.assertEqual(added_item.value, 100)
        mock_save.assert_called_once()

    @patch('app.model.datastorage.json_storage.JSONStorage._save')
    @patch('builtins.open', new_callable=mock_open, read_data='{"TestModel": [{"id": 1, "name": "test", "value": 10}]}')
    def test_update_item(self, mock_file, mock_save):
        storage = JSONStorage('test_data.json')
        updated_item = TestModel(id=1, name='updated', value=20)
        result = storage.update(updated_item)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, 'updated')
        self.assertEqual(result.value, 20)
        mock_save.assert_called_once()

    @patch('app.model.datastorage.json_storage.JSONStorage._save')
    @patch('builtins.open', new_callable=mock_open, read_data='{"TestModel": [{"id": 1, "name": "test", "value": 10}]}')
    def test_remove_item(self, mock_file, mock_save):
        storage = JSONStorage('test_data.json')
        storage.remove(TestModel, 1)
        mock_save.assert_called_once()
        self.assertEqual(len(storage._data['TestModel']), 0)
