from customtkinter import CTkFrame, CTkLabel


class ManageInventory(CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        CTkLabel(master=self, text="مدیریت انبار", font=("B Koodak Bold", 25)).pack(
            fill="x", anchor="center"
        )
