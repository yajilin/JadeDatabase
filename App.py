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

def show_all_options():
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = "SELECT Furniture.Name, Options.Seats, Options.Width, Options.Depth, Options.Height, Options.Price FROM Options LEFT JOIN Furniture ON Options.Product_ID = Furniture.Product_ID;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

def show_options_for_style(Product_ID):

#   menu
while True:
    choice = input("Press 1 to show all styles, press 2 to show all options, press 3 to break: ")

    if choice == "1":
        results = show_all_styles()
        print(results)

    elif choice == "2":
        results = show_all_options()
        print(results)

    elif choice == "3":
        break
