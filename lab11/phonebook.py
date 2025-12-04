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
            cur.execute("CREATE TABLE IF NOT EXISTS phonebook(id SERIAL PRIMARY KEY,name VARCHAR(50),phone VARCHAR(20))")

def insertupdate():
    n=input("name: ")
    p=input("phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name=%s",(n,))
            if cur.fetchone():
                cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s",(p,n))
                print("phone updated")
            else:
                cur.execute("INSERT INTO phonebook(name,phone) VALUES(%s,%s)",(n,p))
                print("user added")
    print("ok")

def search_pattern():
    pattern=input("search pattern: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s",('%'+pattern+'%','%'+pattern+'%'))
            for i in cur.fetchall():
                print(i)

def insert_many_users(users):
    correct=[]
    incorrect=[]

    for u in users:
        name=u[0].strip()
        phone=u[1].strip()

        if phone.isdigit() and len(phone)>=7:
            correct.append((name,phone))
        else:
            incorrect.append((name,phone))

    with connect() as conn:
        with conn.cursor() as cur:
            for name,phone in correct:
                cur.execute("SELECT * FROM phonebook WHERE name=%s",(name,))
                if cur.fetchone():
                    cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s",(phone,name))
                else:
                    cur.execute("INSERT INTO phonebook(name,phone) VALUES(%s,%s)",(name,phone))

    print("Processed:",len(correct))

    if incorrect:
        print("Incorrect phones:")
        for name,phone in incorrect:
            print(name,":",phone)

    print("ok")

def pagination():
    try:
        limit=int(input("limit: "))
        offset=int(input("offset: "))
    except:
        print("numbers only")
        return
    
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY name LIMIT %s OFFSET %s",(limit,offset))
            for i in cur.fetchall():
                print(i)

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
        print("Choose the action:\n"
        "1 ins console\n"
        "2 ins csv\n"
        "3 update\n"
        "4 show all\n"
        "5 filter name\n"
        "6 filter phone\n"
        "7 starts\n"
        "8 contains\n"
        "9 del name\n"
        "10 del phone\n"
        "11 search pattern\n"
        "12 insert multiple\n"
        "13 pagination\n"
        "0 exit")
        x=input("> ")
        if x=="1": insertupdate()
        elif x=="2": insert_csv()
        elif x=="3": update_contact()
        elif x=="4": show_all()
        elif x=="5": filter_name()
        elif x=="6": filter_phone()
        elif x=="7": starts()
        elif x=="8": contains()
        elif x=="9": delete_name()
        elif x=="10": delete_phone()
        elif x=="11": search_pattern()
        elif x=="12":
            users = []
            print("Enter users (name,phone). Type 'done' to finish.")
            while True:
                line = input("> ")
                if line == "done":
                   break
                parts = line.split(",")
                if len(parts) == 2:
                   name = parts[0].strip()
                   phone = parts[1].strip()
                   users.append([name, phone])
                else:
                   print("Use format: name,phone")

            insert_many_users(users)
        elif x=="13": pagination()
        elif x=="0": break

menu()