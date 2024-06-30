from typing import Callable

from customtkinter import CTkLabel, CTkButton, CTkToplevel


class PartDelete(CTkToplevel):
    def __init__(self, callback: Callable, master=None, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.geometry("400x300")
        self.resizable(False, False)

        self.__callback = callback
        CTkLabel(
            master=self, text="حذف جزء غذا", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        CTkButton(self, text="حذف", font=('B Koodak Bold', 25), command=lambda: self.__submit(True)).pack(pady=20,
                                                                                                          side="left",
                                                                                                          padx=35)
        CTkButton(self, text="لغو", font=('B Koodak Bold', 25), command=lambda: self.__submit(False)).pack(pady=20,
                                                                                                           side="right",
                                                                                                           padx=35)

    def __submit(self, confirmed: bool) -> None:
        self.__callback(confirmed)

        self.destroy()
