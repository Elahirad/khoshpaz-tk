from customtkinter import CTkFrame, CTkScrollableFrame, CTkLabel

from .simple_row import SimpleRow


class SimpleTable(CTkFrame):
    def __init__(self, items: list[dict], columns: list[tuple[str, str]], *args, **kw) -> None:
        super().__init__(*args, **kw)
        self._items: list[dict] = items
        self._columns = columns
        self._rows: list[SimpleRow] = []

        self.configure(fg_color='transparent')
        self._table_header = CTkFrame(master=self, fg_color='transparent')
        self._table_header.pack(fill="x", padx=(5, 15))

        self._table_header.grid_columnconfigure(list(range(len(self._columns))), weight=1)

        for idx, col in enumerate(reversed(self._columns)):
            label = CTkLabel(master=self._table_header, text=col[1], font=("B Koodak Bold", 15))
            label.grid(row=0, column=idx, padx=5)

        self._scrollable_frame = CTkScrollableFrame(master=self)
        self._scrollable_frame.pack(fill='both', expand=True)
        self._build_rows(self._items)

    def _build_rows(self, items: list[dict]) -> None:
        self._items = items
        for itemIdx, item in enumerate(self._items):
            row = SimpleRow(item, self._columns, master=self._scrollable_frame)
            row.pack(fill="x")
            self._rows.append(row)
