from typing import Callable

from customtkinter import CTkFrame, CTkScrollableFrame, CTkLabel

from app.view.pages.components.row import Row


class Table(CTkFrame):
    def __init__(self, items: list[dict], columns: list[tuple[str, str]], delete_callback: Callable,
                 update_callback: Callable, *args, **kw) -> None:
        super().__init__(*args, **kw)
        self.__items: list[dict] = items
        self.__columns = columns
        self.__rows: list[Row] = []
        self.__delete_callback = delete_callback
        self.__update_callback = update_callback

        self.configure(fg_color='transparent')
        self.__table_header = CTkFrame(master=self, fg_color='transparent')
        self.__table_header.pack(fill="x", padx=(5, 15))

        self.__table_header.grid_columnconfigure(list(range(2, len(self.__columns) + 2)), weight=2)
        self.__table_header.grid_columnconfigure((0, 1), weight=1)

        for idx, col in enumerate(reversed(self.__columns)):
            label = CTkLabel(master=self.__table_header, text=col[1], font=("B Koodak Bold", 15))
            label.grid(row=0, column=idx + 2, padx=5)

        label = CTkLabel(master=self.__table_header, text='حذف', font=("B Koodak Bold", 15))
        label.grid(row=0, column=0, padx=5)
        label = CTkLabel(master=self.__table_header, text='ویرایش', font=("B Koodak Bold", 15))
        label.grid(row=0, column=1, padx=5)

        self.__scrollable_frame = CTkScrollableFrame(master=self)
        self.__scrollable_frame.pack(fill='both', expand=True)
        self.__build_rows(self.__items)

    def __build_rows(self, items: list[dict]) -> None:
        self.__items = items
        for itemIdx, item in enumerate(self.__items):
            row = Row(item, self.__columns, master=self.__scrollable_frame, delete_callback=self.__delete_callback,
                      update_callback=self.__update_callback)
            row.pack(fill="x")
            self.__rows.append(row)
