import sqlite3

a1 = input("Your name?")
a2 = input("Your Surname?")
a3 = input("Your Profession?")
a4 = int(input("Your Salary?"))

mas1 = [a1,a2,a3,a4]

try:
    sqliteConnection = sqlite3.connect('daulet.db')
    cursor = sqliteConnection.cursor()
    sqlite_select_query = """CREATE TABLE user(name , surname , profession , salary)"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    for i in records:
        print("Name: ", i[0])
        print("Surname: ", i[1])
        print("Profession: ", i[2])
        print("Salary: ", i[3])
        print("\n")

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()


def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('daulet.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from user"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        for i in records:
            print("Name: ", i[0])
            print("Surname: ", i[1])
            print("Profession: ", i[2])
            print("Salary: ", i[3])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()



try:
    sqliteConnection = sqlite3.connect('daulet.db')
    sqlite_insert_query = """INSERT INTO user
                              (name, surname,profession, salary)
                               VALUES (?,?,?,?)"""

    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_insert_query,mas1)
    sqliteConnection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()

o = int(input("You want to show all tables\n1-Yes\n2-No"))

if o == 1:
    readSqliteTable()