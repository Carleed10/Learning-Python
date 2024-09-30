import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS foodstuffs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food TEXT NOT NULL,
        quantity REAL NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO foodstuffs (food, quantity) VALUES
        ("Rice", 3),
        ("Garri", 4),
        ("Beans", 8),
        ("Flour", 7)    
""")

cursor.execute("""
    SELECT * FROM foodstuffs
""")

rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.execute("""
    UPDATE foodstuffs
    SET quantity = 2
    WHERE id = ?
""", (2,))


cursor.execute("""
    SELECT * FROM foodstuffs
""")

rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.execute("""
    DELETE FROM foodstuffs
    WHERE id = ?
""", (3,))


cursor.execute("""
    SELECT * FROM foodstuffs
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()