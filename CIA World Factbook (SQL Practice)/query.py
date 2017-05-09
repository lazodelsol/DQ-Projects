import sqlite3
conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
query = "select name from facts order by population asc;"
results = cursor.execute(query).fetchmany(5)
print(results)