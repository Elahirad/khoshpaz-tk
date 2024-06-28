from customtkinter import CTkFrame, CTkLabel, CTkButton

from app.view.constants import normal_text_font
from app.view.pages.components import Table, InputFrame
from app.view.context import Context


class ManageIngredients(CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__context = Context()
        self.__context.add_callback(self.__update_table)
        self.data = self.__context['ingredients']

        CTkLabel(
            master=self, text="مدیریت مواد اولیه", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        self.__columns = ["نام", "مقدار", "تاریخ ورود", "قیمت"]

        self.__input_frame = InputFrame(self.__columns, self)
        self.__input_frame.pack(pady=10, padx=10, fill="x")

        self.__table = Table(self.data, self.__columns, master=self, width=self.winfo_width(),
                             height=self.winfo_height())
        self.__table.pack(pady=10, padx=10, fill="both", expand=True)

        # Report buttons
        self.__report_frame = CTkFrame(master=self)
        self.__report_frame.pack(pady=10, fill="x")

        self.__report_button1 = CTkButton(master=self.__report_frame, text="۱ گزارش", command=self.__report1,
                                          font=normal_text_font)
        self.__report_button2 = CTkButton(master=self.__report_frame, text="۲ گزارش", command=self.__report2,
                                          font=normal_text_font)
        self.__report_button3 = CTkButton(master=self.__report_frame, text="۳ گزارش", command=self.__report3,
                                          font=normal_text_font)
        self.__report_button1.pack(side="right", padx=5)
        self.__report_button2.pack(side="right", padx=5)
        self.__report_button3.pack(side="right", padx=5)

    def __update_table(self):
        self.data = self.__context['ingredients']
        self.__table.pack_forget()
        self.__report_frame.pack_forget()
        self.__table = Table(self.data, self.__columns, master=self, width=self.winfo_width(),
                             height=self.winfo_height())
        self.__table.pack(pady=10, padx=10, fill="both", expand=True)
        self.__report_frame.pack(pady=10, fill="x")

    def __report1(self): print("۱ گزارش اجرا شد")

    def __report2(self): print("۲ گزارش اجرا شد")

    def __report3(self): print("۳ گزارش اجرا شد")
