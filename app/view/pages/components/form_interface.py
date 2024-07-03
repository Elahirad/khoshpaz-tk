from abc import ABC, abstractmethod
from typing import Callable

from customtkinter import CTkLabel, CTkToplevel

from app.view.context import Context


class IForm(CTkToplevel, ABC):
    def __init__(self, title: str, default_values: dict[str, str], callback: Callable, *args,
                 **kwargs) -> None:
        super().__init__(master=None, *args, **kwargs)
        self.geometry("400x700")
        self.resizable(False, False)

        self._context = Context()

        self._current_values = default_values

        self._callback = callback
        CTkLabel(
            master=self, text=title, font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

    @abstractmethod
    def _submit(self) -> None:
        pass
