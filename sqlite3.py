import sqlite3

# 1. Connect to database (creates file if not exists)
conn = sqlite3.connect("mydata.db")

# 2. Create a cursor (to run SQL commands)
cursor = conn.cursor()

# 3. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# 4. Insert some data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Ali", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Sara", 22))

# 5. Save changes
conn.commit()

# 6. Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)   # [(1, 'Ali', 20), (2, 'Sara', 22)]

# 7. Close connection
conn.close()