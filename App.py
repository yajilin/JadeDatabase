#   main application for database
import sqlite3

#   functions
def show_all_styles():
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Furniture;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

#   menu
while True:
    choice = input("Press 1 to show all styles, press 2 to break: ")

    if choice == "1":
        results = show_all_styles()
        print(results)

    elif choice == "2":
        break
