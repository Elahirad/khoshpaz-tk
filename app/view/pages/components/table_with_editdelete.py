from typing import Callable

from customtkinter import CTkFrame, CTkScrollableFrame, CTkLabel

from app.view.pages.components.editable_deletable_row import EditableDeletableRow


class TableWithEditDelete(CTkFrame):
    def __init__(self, items: list[dict], columns: list[tuple[str, str]], delete_callback: Callable,
                 update_callback: Callable, *args, **kw) -> None:
        super().__init__(*args, **kw)
        self._items: list[dict] = items
        self._columns = columns
        self._rows: list[EditableDeletableRow] = []
        self._delete_callback = delete_callback
        self._update_callback = update_callback

        self.configure(fg_color='transparent')
        self._table_header = CTkFrame(master=self, fg_color='transparent')
        self._table_header.pack(fill="x", padx=(5, 15))

        self._table_header.grid_columnconfigure(list(range(2, len(self._columns) + 2)), weight=2)
        self._table_header.grid_columnconfigure((0, 1), weight=1)

        for idx, col in enumerate(reversed(self._columns)):
            label = CTkLabel(master=self._table_header, text=col[1], font=("B Koodak Bold", 15))
            label.grid(row=0, column=idx + 2, padx=5)

        label = CTkLabel(master=self._table_header, text='حذف', font=("B Koodak Bold", 15))
        label.grid(row=0, column=0, padx=5)
        label = CTkLabel(master=self._table_header, text='ویرایش', font=("B Koodak Bold", 15))
        label.grid(row=0, column=1, padx=5)

        self._scrollable_frame = CTkScrollableFrame(master=self)
        self._scrollable_frame.pack(fill='both', expand=True)
        self._build_rows(self._items)

    def _build_rows(self, items: list[dict]) -> None:
        self._items = items
        for itemIdx, item in enumerate(self._items):
            row = EditableDeletableRow(item, self._columns, master=self._scrollable_frame,
                                       delete_callback=self._delete_callback,
                                       update_callback=self._update_callback)
            row.pack(fill="x")
            self._rows.append(row)
