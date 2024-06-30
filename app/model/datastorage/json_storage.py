import json
from typing import Type, TypeVar, List, Optional
from app.model.datastorage.interface import IDataStorage

T = TypeVar('T')


class JSONStorage(IDataStorage):
    def __init__(self, filename: str):
        self._filename = filename
        self._data = {}
        self._next_id = {}
        self._load()

    def _load(self):
        try:
            with open(self._filename, 'r') as file:
                self._data = json.load(file)
                # Initialize next_id for each model from loaded data
                for model_name, items in self._data.items():
                    self._next_id[model_name] = max(item['id'] for item in items) + 1 if items else 1
        except FileNotFoundError:
            self._data = {}

    def _save(self):
        with open(self._filename, 'w') as file:
            json.dump(self._data, file, default=lambda o: o.__dict__)

    def _get_next_id(self, model_name: str) -> int:
        if model_name not in self._next_id:
            self._next_id[model_name] = 1
        next_id = self._next_id[model_name]
        self._next_id[model_name] += 1
        return next_id

    def get_all(self, model_class: Type[T]) -> List[T]:
        model_name = model_class.__name__
        return [model_class(**item) for item in self._data.get(model_name, [])]

    def get(self, model_class: Type[T], item_id: int) -> Optional[T]:
        model_name = model_class.__name__
        for item in self._data.get(model_name, []):
            if item['id'] == item_id:
                return model_class(**item)
        return None

    def add(self, item: T) -> T:
        model_name = item.__class__.__name__
        if model_name not in self._data:
            self._data[model_name] = []
        item_dict = item.__dict__.copy()
        item_dict['id'] = self._get_next_id(model_name)
        self._data[model_name].append(item_dict)
        self._save()
        return item.__class__(**item_dict)

    def update(self, item: T) -> T:
        model_name = item.__class__.__name__
        for idx, existing in enumerate(self._data.get(model_name, [])):
            if existing['id'] == item.id:
                self._data[model_name][idx] = item.__dict__
                self._save()
                return item
        raise ValueError(f'Item with id {item.id} not found in {model_name}')

    def remove(self, model_class: Type[T], item_id: int) -> None:
        model_name = model_class.__name__
        self._data[model_name] = [
            item for item in self._data.get(model_name, []) if item['id'] != item_id
        ]
        self._save()
