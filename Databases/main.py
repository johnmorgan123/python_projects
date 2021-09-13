import sqlite3
import psycopg2

def get_connection():
    return psycopg2.connect("dbname='john' user='john' password='channel12' host='pg.john'")

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = get_connection()
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)" , (item, quantity, price))
    conn.commit()
    conn.close()



def view():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s ", (quantity, price, item))
    conn.commit()
    conn.close()

#update(11, 6, "Water Glass")
#delete("Wine Glass")
#print(view())

create_table()
#insert("Potato", 13, 19)
#delete("Potato")
update(20, 15, 'Apple')
print(view())