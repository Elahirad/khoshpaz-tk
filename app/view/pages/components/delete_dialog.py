from typing import Callable

from customtkinter import CTkLabel, CTkButton, CTkToplevel


class DeleteDialog(CTkToplevel):
    def __init__(self, title: str, callback: Callable, master=None, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.geometry("400x300")
        self.resizable(False, False)

        self._callback = callback
        CTkLabel(
            master=self, text=title, font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        CTkButton(self, text="حذف", font=('B Koodak Bold', 25), command=lambda: self._submit(True)).pack(pady=20,
                                                                                                         side="left",
                                                                                                         padx=35)
        CTkButton(self, text="لغو", font=('B Koodak Bold', 25), command=lambda: self._submit(False)).pack(pady=20,
                                                                                                          side="right",
                                                                                                          padx=35)

    def _submit(self, confirmed: bool) -> None:
        self._callback(confirmed)

        self.destroy()
