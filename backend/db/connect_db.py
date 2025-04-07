import mysql.connector

DB_CONNECTION = None

def get_db():
    global DB_CONNECTION
    
    if DB_CONNECTION is None:
        connect_db()
    
    return DB_CONNECTION

def connect_db():
    global DB_CONNECTION
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="quiz"
    )

    print("Successfully connected to the database")

    DB_CONNECTION = db

def get_cursor():
    db = get_db()
    cursor = db.cursor()
    return cursor