import sqlite3

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

# Insert sample data into the user table
sample_users = [
    ('John Doe',),
    ('Jane Smith',),
    ('Alice Johnson',),
    ('Bob Brown',),
    ('Charlie Davis',),
    ('Diana Prince',),
    ('Ethan Hunt',),
    ('Fiona Apple',),
    ('George Washington',),
    ('Hannah Montana',)
]

# Insert sample users into the table
cursor.executemany('INSERT INTO user (name) VALUES (?)', sample_users)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and sample data created successfully.")