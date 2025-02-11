### 1. To check  if the App is Installed on Any Site:
**bench --site yoursite list-apps**
### 2. to see app details :
**nano ~/frappe-bench-14/sites/apps.txt**
### 3. Delete the App from apps/ Directory
**rm -rf ~/frappe-bench-14/apps/library_management**

### 4.  bench build and restart 
**bench build – Compiles and optimizes frontend assets (JavaScript, CSS) for all installed apps.**\n
**bench restart – Restarts all Frappe processes to apply changes and free up system resources.**

