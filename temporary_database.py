import sqlite3

conn = sqlite3.connect("store.db")
c= conn.cursor()
c.execute('''INSERT INTO managers (full_name,contact,address,email,password) VALUES ("pema",9808338762,"boudha","ws",123)''')
conn.commit()
conn.close()   