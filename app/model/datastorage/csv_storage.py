import csv
import os
from typing import Type, TypeVar, List, Optional, Dict, Any
from app.model.datastorage.interface import IDataStorage
from dataclasses import fields, asdict

T = TypeVar('T')


class CSVStorage(IDataStorage):
    def __init__(self, directory: str):
        self._directory = directory
        self._next_id = {}

        if not os.path.exists(directory):
            os.makedirs(directory)

    def _get_file_path(self, model_name: str) -> str:
        return os.path.join(self._directory, f"{model_name}.csv")

    def _load_data(self, model_name: str) -> List[Dict[str, Any]]:
        file_path = self._get_file_path(model_name)
        if not os.path.exists(file_path):
            return []

        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]

    def _save_data(self, model_name: str, data: List[Dict[str, Any]]) -> None:
        file_path = self._get_file_path(model_name)
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            if data:
                writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

    def _get_next_id(self, model_name: str) -> int:
        if model_name not in self._next_id:
            data = self._load_data(model_name)
            if data:
                self._next_id[model_name] = max(int(item['id']) for item in data) + 1
            else:
                self._next_id[model_name] = 1
        next_id = self._next_id[model_name]
        self._next_id[model_name] += 1
        return next_id

    def get_all(self, model_class: Type[T]) -> List[T]:
        model_name = model_class.__name__
        data = self._load_data(model_name)
        return [model_class(**{field.name: self.__convert_type(field.type, item[field.name])
                               for field in fields(model_class)}) for item in data]

    def get(self, model_class: Type[T], item_id: int) -> Optional[T]:
        model_name = model_class.__name__
        data = self._load_data(model_name)
        for item in data:
            if int(item['id']) == item_id:
                return model_class(**{field.name: self.__convert_type(field.type, item[field.name])
                                      for field in fields(model_class)})
        return None

    def add(self, item: T) -> T:
        model_name = item.__class__.__name__
        item_dict = asdict(item)
        item_dict['id'] = self._get_next_id(model_name)
        data = self._load_data(model_name)
        data.append(item_dict)
        self._save_data(model_name, data)
        return item.__class__(**item_dict)

    def update(self, item: T) -> T:
        model_name = item.__class__.__name__
        item_dict = asdict(item)
        data = self._load_data(model_name)
        for idx, existing in enumerate(data):
            if int(existing['id']) == item.id:
                data[idx] = item_dict
                self._save_data(model_name, data)
                return item
        raise ValueError(f'Item with id {item.id} not found in {model_name}')

    def remove(self, model_class: Type[T], item_id: int) -> None:
        model_name = model_class.__name__
        data = self._load_data(model_name)
        data = [item for item in data if int(item['id']) != item_id]
        self._save_data(model_name, data)

    @staticmethod
    def __convert_type(field_type, value):
        if field_type == int:
            return int(value)
        elif field_type == float:
            return float(value)
        elif field_type == list:
            return eval(value)
        elif field_type == str:
            return value
        return eval(value)
