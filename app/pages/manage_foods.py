from customtkinter import CTkFrame, CTkLabel


class ManageFoods(CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        CTkLabel(master=self, text="مدیریت غذاها", font=("B Koodak Bold", 25)).pack(
            fill="x", anchor="center"
        )