import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('CREATE TABLE students (name text, mark real)')
c.execute("INSERT INTO students VALUES ('asok',80.50)")
c.execute("INSERT INTO students VALUES ('john',78.20)")
c.execute("INSERT INTO students VALUES ('rahul',67.10)")

conn.commit()
conn.close()

