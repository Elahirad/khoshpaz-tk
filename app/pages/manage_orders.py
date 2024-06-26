from customtkinter import CTkFrame, CTkLabel


class ManageOrders(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CTkLabel(master=self, text="مدیریت سفارش‌ها", font=("B Koodak Bold", 25)).pack(
            fill="x", anchor="center"
        )
