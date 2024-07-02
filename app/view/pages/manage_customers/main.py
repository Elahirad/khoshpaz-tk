from customtkinter import CTkButton

from app.view.constants import normal_text_font
from app.view.pages.components import IDataView
from .customer_form import CustomerForm


class ManageCustomers(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('customers', 'مشتری', 'مشتریان', [('name', 'نام'), ('last_name', 'نام خانوادگی')],
                         {'id': 0, 'name': '', 'last_name': ''}, CustomerForm, *args, **kwargs)

        self._report_frame.pack_forget()

    def _update_table(self):
        super()._update_table()
        self._report_frame.pack_forget()

    def _add_callback(self, data):
        self._context.controller.add_customer(data['name'], data['last_name'])

    def _delete_callback(self, confirmed: bool, entity_id: int):
        if confirmed:
            self._context.controller.remove_customer(entity_id)

    def _update_callback(self, entity_id, data):
        self._context.controller.update_customer(entity_id, data['name'], data['last_name'])
