# import frappe
from frappe.model.document import Document

class FlightPassenger1(Document):
  def before_save(self):
    if self.first_name and self.last_name:
        self.full_name = f"{self.first_name} {self.last_name}"
