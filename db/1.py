import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# show client name, count of orders, total amount of orders
# for clients who made more than 1 order
query = """
-- write query here
"""

cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)

conn.close()
