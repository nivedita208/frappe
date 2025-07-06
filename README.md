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


ERPNext: Bench Restart & Setup Troubleshooting Log  
===================================================

📅 Date: July 6, 2025  
👩‍💻 System: Ubuntu + Frappe Bench v14  

---------------------------------------------------  
🧩 Issue 1: supervisorctl Error – unix:///var/run/supervisor.sock no such file  
---------------------------------------------------  
Cause:  
- Supervisor service was not running.

✅ Solution:
    sudo systemctl start supervisor  
    sudo systemctl enable supervisor  

---------------------------------------------------  
🧩 Issue 2: Supervisor failed to start – supervisord.log does not exist  
---------------------------------------------------  
Cause:  
- Missing log directory for Supervisor.

✅ Solution:
    sudo mkdir -p /var/log/supervisor  
    sudo systemctl restart supervisor  

---------------------------------------------------  
🧩 Issue 3: bench restart failed – no such file for frappe  
---------------------------------------------------  
Cause:  
- Old supervisor config was missing or misconfigured.

✅ Solution:
    bench setup supervisor  
    sudo supervisorctl reread  
    sudo supervisorctl update  

---------------------------------------------------  
🧩 Issue 4: frappe-bench-node-socketio: ERROR (spawn error)  
---------------------------------------------------  
Causes:  
- Node.js/Yarn not installed properly  
- Port 9000 already in use

✅ Solution:
    node -v  
    yarn -v  
    sudo lsof -i :9000  
    bench restart  

---------------------------------------------------  
🧩 Issue 5: bench setup requirements failed – README.md or flit_core missing  
---------------------------------------------------  
Causes:  
- Custom app missing README.md  
- No internet during install (for flit_core)

✅ Solution:
    touch apps/frappe/README.md  
    (or for other apps, e.g. airplane_mode)  
    Fix internet connection  
    bench setup requirements  

---------------------------------------------------  
🧩 Issue 6: bench doctor shows ValueError: Unknown type <class 'NoneType'>  
---------------------------------------------------  
Cause:  
- Redis worker registry has invalid or stale keys.

✅ Solution:
    redis-cli --scan --pattern "rq:worker*" | xargs redis-cli del  
    bench restart  

---------------------------------------------------  
🧠 When to Use bench restart  
---------------------------------------------------  
| Situation                    | Bench Restart Required? |
|-----------------------------|--------------------------|
| Server Script (via UI)      | ❌ No                    |
| Client Script (via UI)      | ❌ No                    |
| Python code (.py files)     | ✅ Yes                   |
| JavaScript (.js files)      | ✅ Yes                   |
| New site/app or supervisor  | ✅ Yes                   |

---------------------------------------------------  
🟢 Final Working Output After Fixing Everything  
---------------------------------------------------  

bench restart

frappe-bench-web:frappe-bench-node-socketio: started  
frappe-bench-web:frappe-bench-frappe-web: started  
frappe-bench-workers:frappe-bench-frappe-schedule: started  
frappe-bench-workers:frappe-bench-frappe-short-worker-0: started  
frappe-bench-workers:frappe-bench-frappe-long-worker-0: started  

✅ All services are now running properly!
