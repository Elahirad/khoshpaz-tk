from abc import ABC, abstractmethod
from typing import Type, TypeVar, List, Optional

T = TypeVar('T')


class IDataStorage(ABC):
    @abstractmethod
    def get_all(self, model_class: Type[T]) -> List[T]: pass

    @abstractmethod
    def get(self, model_class: Type[T], item_id: int) -> Optional[T]: pass

    @abstractmethod
    def add(self, item: T) -> T: pass

    @abstractmethod
    def update(self, item: T) -> T: pass

    @abstractmethod
    def remove(self, model_class: Type[T], item_id: int) -> None: pass
