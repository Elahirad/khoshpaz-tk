from abc import ABC, abstractmethod
from customtkinter import CTk


class IApp(ABC, CTk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mode: int = 0

    @abstractmethod
    def switch_mode(self, mode: int) -> None: pass


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass
