# frappe
# classes in frappe
| **Class**                  | **Purpose**                                          | **Example Usage** |
|----------------------------|------------------------------------------------------|------------------|
| **`frappe.ui.Dialog`**      | Creates and manages pop-up modals (dialogs).       | `const dialog = new frappe.ui.Dialog({ title: "Example", fields: [{ label: "Name", fieldname: "name", fieldtype: "Data" }] }); dialog.show();` |
| **`frappe.ui.form.Form`**   | Represents a form in Frappe, allows form interactions. | `frappe.ui.form.on("Sales Invoice", { refresh: function(frm) { console.log(frm.doc); } });` |
| **`frappe.ui.Field`**       | Represents an individual field in a form or dialog. | `let field = frm.get_field("customer"); field.df.read_only = 1; field.refresh();` |
| **`frappe.ui.toolbar`**     | Manages the top navigation bar (toolbar). | `frappe.ui.toolbar.add_dropdown_button("Custom", "Click Me", function() { frappe.msgprint("Clicked!"); });` |
| **`frappe.model.get_value()`** | Fetches a specific field value from a document. | `frappe.model.get_value("Customer", "CUST-0001", "customer_name", value => { console.log(value); });` |
| **`frappe.model.set_value()`** | Updates a specific field value dynamically. | `frappe.model.set_value("Sales Invoice", "INV-0001", "customer", "New Customer");` |
| **`frappe.db.get_doc()`**    | Retrieves an entire document from the database. | `frappe.db.get_doc("Customer", "CUST-0001").then(doc => { console.log(doc.customer_name); });` |
| **`frappe.db.insert()`**     | Inserts a new document into the database. | `frappe.db.insert({doctype: "Customer", customer_name: "New Cust"}).then(doc => { console.log("Inserted:", doc.name); });` |
