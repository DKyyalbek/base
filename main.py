# import sqlite3
#
# a1 = input("Your name?")
# a2 = input("Your Surname?")
# a3 = input("Your Profession?")
# a4 = int(input("Your Salary?"))
#
# mas1 = [a1,a2,a3,a4]
#
# try:
#     sqliteConnection = sqlite3.connect('daulet.db')
#     cursor = sqliteConnection.cursor()
#     sqlite_select_query = """CREATE TABLE user(name , surname , profession , salary)"""
#     cursor.execute(sqlite_select_query)
#     records = cursor.fetchall()
#     print("Total rows are:  ", len(records))
#     for i in records:
#         print("Name: ", i[0])
#         print("Surname: ", i[1])
#         print("Profession: ", i[2])
#         print("Salary: ", i[3])
#         print("\n")
#
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Failed to read data from sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#
#
# def readSqliteTable():
#     try:
#         sqliteConnection = sqlite3.connect('daulet.db')
#         cursor = sqliteConnection.cursor()
#         sqlite_select_query = """SELECT * from user"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Total rows are:  ", len(records))
#         for i in records:
#             print("Name: ", i[0])
#             print("Surname: ", i[1])
#             print("Profession: ", i[2])
#             print("Salary: ", i[3])
#             print("\n")
#
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Failed to read data from sqlite table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#
#
#
# try:
#     sqliteConnection = sqlite3.connect('daulet.db')
#     sqlite_insert_query = """INSERT INTO user
#                               (name, surname,profession, salary)
#                                VALUES (?,?,?,?)"""
#
#     cursor = sqliteConnection.cursor()
#     cursor.execute(sqlite_insert_query,mas1)
#     sqliteConnection.commit()
#
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#
# o = int(input("You want to show all tables\n1-Yes\n2-No"))
#
# if o == 1:
#     readSqliteTable()



# try:
#     sqliteConnection = sqlite3.connect('gulder.db')
#     sqlite_create_table_query = '''CREATE TABLE gul (
#                                 name text,
#                                 shtuk integer,
#                                 price integer);'''
#
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")
#     cursor.execute(sqlite_create_table_query)
#     sqliteConnection.commit()
#     print("SQLite table created")
#
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("sqlite connection is closed")





import operator
import random
import turtle
import sqlite3


class Gul():
    def __init__(self, name, shtuk, price):
        self.name = name
        self.shtuk = shtuk
        self.price = price

    def show(self):
        print('Названия цветок: {}'
              ' Штук: {} штук'
              ' Цена: {} тг'.format(self.name, self.shtuk, self.price))

def sort_choice(Data, choice):
    result = sorted(Data, key=operator.attrgetter(choice))
    for i in result:
        i.show()

class Magaz(Gul):
    def __init__(self, name, shtuk, price):
        super().__init__(name, shtuk, price)


gul1 = Magaz('Roza', 50, 5000)
gul2 = Magaz('BakBak', 150, 2000)
gul3 = Magaz('Lala',100, 3500)
e = [gul1, gul2, gul3]
mas = []
# try:
#     for i in e:
#         mas = [i.name,i.shtuk,i.price]
#
#
#         sqliteConnection = sqlite3.connect('gulder.db')
#         sqlite_insert_query = """INSERT INTO gul
#                               (name,shtuk,price)
#                                VALUES(?,?,?)"""
#
#         cursor = sqliteConnection.cursor()
#         cursor.execute(sqlite_insert_query,mas)
#         sqliteConnection.commit()
#
#         cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('gulder.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from gul"""
        cursor.execute(sqlite_select_query)
        e = cursor.fetchall()
        print("Total rows are:  ", len(e))
        for i in e:
            print("Name: ", i[0])
            print("Shtuk: ", i[1])
            print("Price: ", i[2])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


readSqliteTable()

t = []
def su(t):
    r = sqlite3.connect("gulder.db")
    price = r.execute("select price from gul")
    pr = price.fetchall()
    for i in pr:
        t.append(i[0])
    r.close()
su(t)

print(t)
def ajj(t):
    d = int(input("Kansha akshaga alasiz - "))
    if 0 < d < 2000:
        print("Norm Buket Zhok")
        print("Try again?")
        return ajj(t)
    elif d < 0:
        print("Minus san")
        print("Try again?")
        return ajj(t)
    else:
        r = [0]
        i = 0
        g = 0
        while g <= d:
            if e[0].shtuk == 0 or e[1].shtuk == 0 or e[2].shtuk == 0:
                print("Gul sany zhetpid")
            else:
                r.append(random.choice(t))
            i = i + 1
            if g <= d:
                g = g + r[i]
            if g > d:
                r.pop(-1)
        y = 0
        for i in range(len(r)):
            y = y + r[i]
        print(y)
        t = []
        mas = []
        su(t)
        print(r)
        for i in range(len(t)):
            a = 0
            for j in range(len(r)):
                if r[j] == t[i]:
                    a = a + 1
            mas.append(a)

        r = sqlite3.connect("gulder.db")
        cursor = r.execute("select count(*) from gul")
        values = cursor.fetchone()
        len = values[0]
        a = r.execute("select name from gul")
        name = a.fetchall()
        print(name[0])
        for i in range(len):
            print(name[i], mas[i], "Dana")

        print("Alatin boldinizba?")
        print("1. Ya")
        print("2. Zhok")
        a = int(input())
        if a == 1:
            for i in range(len(e)):
                e[i].shtuk = e[i].shtuk - mas[i]
            # guu()
            print("Kalgan akshanyz - ", d - y)
        if a == 2:
            return ajj(t)


def ahh():
    print("Alatin boldinizba?")
    print("1. Ya")
    print("2. Zhok")
    a = int(input())
    if a == 1:
        for i in range(len(e)):
            e[i].shtuk = e[i].shtuk - mas[i]
        # guu()
    if a == 2:
        return ajj(t)

mas = []
def du(mas):
    for i in range(len(e)):
        a = int(input(e[i].name + " Kansh shtuk - "))
        if a <= e[i].shtuk:
            mas.append(a)
        else:
            print("ondai olshemde gul zhok zhazdynyz")
            return du(mas)

    for i in range(len(e)):
        print(e[i].name, mas[i], "Dana")

    ahh()
while True:

    print('1. Barlyk Gulder')
    print('2. Satyp Alamyn ! ')
    print('3. Admin')
    print('4. exit')

    n = int(input())
    if n == 1:
        sort_choice(e, 'shtuk')

    if n == 2:
        while True:
            print('Guldi kalai aluga bolady?')
            print('1. Kolda bar aksha boinsha!')
            print('2. Bagasy boinsha!')
            print("3. Exit!")
            o = int(input())
            if o == 1:
                su(t)
                ajj(t)
            if o == 2:
                sort_choice(e, "shtuk")
                mas = []
                du(mas)


            if o == 3:
                break
    if n == 3:
        print("Zhana gul keldy!")
        a = int(input("Kelgen gul turlerinin sany? "))
        for i in range(a):
            a1 = input("Gul aty?")
            a2 = int(input("Gul sany?"))
            a3 = int(input("Gul bagasy?"))
            r = 0
            for i in e:
                if a1.strip() == i.name:
                    i.shtuk = i.shtuk + a2
                    print("1 - Buringi baga kalsinba?")
                    print("2 - Osi baga bagaga 25 %?")
                    if i.price != a3:
                        f = int(input())
                        if f == 1:
                            continue
                        if f == 2:
                            i.price = a3 + a3 * 0.25
                    else:
                        continue
                else:
                    r = r + 1
            if r == len(e):
                w = Magaz(a1, a2, a3)
                e.append(w)

        for i in e:
            i.show()
    if n == 4:
        break


