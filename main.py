from app import AppView
from app.model.datastorage import JSONStorage
from app.controller import Controller
from app.model import Ingredient

if __name__ == "__main__":
    app = AppView(controller=None)
    ds = JSONStorage("data.json")
    controller = Controller(view=app, data_storage=ds)
    app.mainloop()

