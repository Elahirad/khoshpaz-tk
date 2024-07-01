import unittest
from unittest.mock import patch, mock_open
from app.model.datastorage.csv_storage import CSVStorage
from app.model.types import Customer  # Assuming types.py contains Customer dataclass
from dataclasses import dataclass, asdict


@dataclass
class TestModel:
    __test__ = False
    id: int
    name: str
    value: int


class TestCSVStorage(unittest.TestCase):

    def setUp(self):
        self.directory = 'test_directory'
        self.storage = CSVStorage(self.directory)

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='id,name,value\n1,test,10\n')
    def test_get_all(self, mock_file, mock_exists):
        items = self.storage.get_all(TestModel)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].id, 1)
        self.assertEqual(items[0].name, 'test')
        self.assertEqual(items[0].value, 10)

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='id,name,value\n1,test,10\n')
    def test_get_existing_item(self, mock_file, mock_exists):
        item = self.storage.get(TestModel, 1)
        self.assertIsNotNone(item)
        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, 'test')
        self.assertEqual(item.value, 10)

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='id,name,value\n1,test,10\n')
    def test_get_non_existing_item(self, mock_file, mock_exists):
        item = self.storage.get(TestModel, 2)
        self.assertIsNone(item)

    @patch('app.model.datastorage.csv_storage.CSVStorage._save_data')
    @patch('app.model.datastorage.csv_storage.CSVStorage._load_data', return_value=[])
    @patch('app.model.datastorage.csv_storage.CSVStorage._get_next_id', return_value=1)
    def test_add_item(self, mock_get_next_id, mock_load_data, mock_save_data):
        new_item = TestModel(id=0, name='new', value=100)
        added_item = self.storage.add(new_item)
        self.assertEqual(added_item.id, 1)
        self.assertEqual(added_item.name, 'new')
        self.assertEqual(added_item.value, 100)
        mock_save_data.assert_called_once()

    @patch('app.model.datastorage.csv_storage.CSVStorage._save_data')
    @patch('app.model.datastorage.csv_storage.CSVStorage._load_data',
           return_value=[{'id': '1', 'name': 'test', 'value': '10'}])
    def test_update_item(self, mock_load_data, mock_save_data):
        updated_item = TestModel(id=1, name='updated', value=20)
        result = self.storage.update(updated_item)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, 'updated')
        self.assertEqual(result.value, 20)
        mock_save_data.assert_called_once()

    @patch('app.model.datastorage.csv_storage.CSVStorage._save_data')
    @patch('app.model.datastorage.csv_storage.CSVStorage._load_data',
           return_value=[{'id': '1', 'name': 'test', 'value': '10'}])
    def test_remove_item(self, mock_load_data, mock_save_data):
        self.storage.remove(TestModel, 1)
        mock_save_data.assert_called_once()
        remaining_data = mock_save_data.call_args[0][1]
        self.assertEqual(len(remaining_data), 0)
