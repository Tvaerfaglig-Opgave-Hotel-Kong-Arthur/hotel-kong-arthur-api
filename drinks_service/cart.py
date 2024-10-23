import sqlite3

DB_NAME = 'drinks.db'

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        # ----------------------------- QUERY SHOULD BE UPDATED
        create_table_query = """
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            amount INTEGER
        )
        """
        
        # Execute the create table statement
        cur.execute(create_table_query)
