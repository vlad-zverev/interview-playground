import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
)
"""
)

cursor.execute("INSERT INTO customers (name) VALUES ('Alice')")
cursor.execute("INSERT INTO customers (name) VALUES ('Bob')")
cursor.execute("INSERT INTO customers (name) VALUES ('Charlie')")

cursor.execute(
    "INSERT INTO orders (customer_id, amount, order_date) VALUES (1, 100.0, '2024-01-01')"
)
cursor.execute(
    "INSERT INTO orders (customer_id, amount, order_date) VALUES (1, 150.0, '2024-02-01')"
)
cursor.execute(
    "INSERT INTO orders (customer_id, amount, order_date) VALUES (2, 200.0, '2024-01-15')"
)
cursor.execute(
    "INSERT INTO orders (customer_id, amount, order_date) VALUES (3, 50.0, '2024-01-20')"
)
cursor.execute(
    "INSERT INTO orders (customer_id, amount, order_date) VALUES (3, 80.0, '2024-02-10')"
)

conn.commit()
conn.close()
