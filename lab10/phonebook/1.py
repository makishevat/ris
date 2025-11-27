import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Malika123)"
    )

def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE phonebook(id SERIAL PRIMARY KEY," \
                                                "name VARCHAR(50)," \
                                                "phone VARCHAR(20))")

def insert_console():
    n=input("name: ")
    p=input("phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook(name,phone) VALUES(%s,%s)",(n,p))
    print("ok")

def insert_csv():
    with connect() as conn:
        with conn.cursor() as cur:
            with open("data.csv") as f:
                r=csv.reader(f)
                cur.executemany("INSERT INTO phonebook(name,phone) VALUES(%s,%s)",r)
    print("ok")

def update_contact():
    n=input("old name: ")
    print("1 new name")
    print("2 new phone")
    x=input("> ")
    if x=="1":
        v=input("new name: ")
        q="UPDATE phonebook SET name=%s WHERE name=%s"
        p=(v,n)
    else:
        v=input("new phone: ")
        q="UPDATE phonebook SET phone=%s WHERE name=%s"
        p=(v,n)
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(q,p)
    print("ok")

def show_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            for i in cur.fetchall():
                print(i)

def filter_name():
    n=input("name: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name=%s",(n,))
            for i in cur.fetchall():
                print(i)

def filter_phone():
    p=input("phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE phone=%s",(p,))
            for i in cur.fetchall():
                print(i)

def starts():
    s=input("starts: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name LIKE %s",(s+"%",))
            for i in cur.fetchall():
                print(i)

def contains():
    c=input("contains: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s",("%"+c+"%",))
            for i in cur.fetchall():
                print(i)

def delete_name():
    n=input("delete name: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE name=%s",(n,))
    print("ok")

def delete_phone():
    p=input("delete phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE phone=%s",(p,))
    print("ok")

def menu():
    create_table()
    while True:
        print("1 ins console")
        print("2 ins csv")
        print("3 update")
        print("4 show all")
        print("5 filter name")
        print("6 filter phone")
        print("7 starts")
        print("8 contains")
        print("9 del name")
        print("10 del phone")
        print("0 exit")
        x=input("> ")
        if x=="1": insert_console()
        elif x=="2": insert_csv()
        elif x=="3": update_contact()
        elif x=="4": show_all()
        elif x=="5": filter_name()
        elif x=="6": filter_phone()
        elif x=="7": starts()
        elif x=="8": contains()
        elif x=="9": delete_name()
        elif x=="10": delete_phone()
        elif x=="0": break

menu()
