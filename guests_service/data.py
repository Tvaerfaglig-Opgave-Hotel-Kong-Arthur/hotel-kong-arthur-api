import sqlite3
import csv

DB_NAME = 'data.db'
TABLE_NAME = 'guests'

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            family_name TEXT,
            country TEXT,
            UNIQUE(first_name, family_name, country)
        )
        """
        
        # Execute the create table statement
        cur.execute(create_table_query)

def add_csv_to_db(filepath):
    with open(filepath, mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile) # Spring headeren over
        for line in csvFile:
                #print(line)
                data = {
                    "first_name": line[0] if line[0] else None,
                    "family_name": line[1] if line[1] else None,
                    "country": line[2] if line[2] else None,
                }
                add_new_item(data)
    return

def add_new_item(data):
    try:
        # Connect to db/file - both read or create if not exists
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            
            cur.execute(
                f'''
                INSERT OR IGNORE INTO {TABLE_NAME}
                (first_name, family_name, country) 
                VALUES (?, ?, ?)
                ''',
                (
                    data.get('first_name'),
                    data.get('family_name'),
                    data.get('country')
                )
            )

            return [201, {"message": "New item added to database successfully."}]

    except sqlite3.Error as e:
        return [500, {"error": str(e)}]

def update_item(id, data):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            
            query = f'''
            UPDATE {TABLE_NAME}
            SET '''

            i = 0
            for key,value in data.items():
                if key not in query:
                    if i > 0:
                        query+= ", "

                    if isinstance(value, str):
                        query += f'{key} = "{value}"'
                    else:
                        query += f'{key} = {value}'
                    i += 1

            query += f" WHERE id = {id}"
            print(query)

            cur.execute(query)
            if cur.rowcount == 0:
                return [404, {"message": "Guest not found."}]
            
            return [200, {"message": "Guest updated successfully."}]

    except sqlite3.Error as e:
        return [500, {"error": str(e)}]


def select_all_items():
    try:
        # Connect to db/file - both read or create if not exists
        with sqlite3.connect(DB_NAME) as conn:
            # Set the row factory to sqlite3.Row - By setting conn.row_factory = sqlite3.Row, you tell SQLite to return rows as sqlite3.Row objects, which can be accessed like dictionaries.
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM {TABLE_NAME}')

            # Fetch all rows and convert them to dictionaries
            data = cur.fetchall()
        
            if data:
                return [200, [dict(row) for row in data]]
            else:
                return [204, {"message": f"No items in {TABLE_NAME}"}]
    
    except sqlite3.Error as e:
        return [500, {"error": str(e)}]


def delete_item_by_id(id):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()

            # Delete the row with the specified id
            cur.execute(f'DELETE FROM {TABLE_NAME} WHERE id = ?', (id,))
            
            if cur.rowcount == 0:
                return [404, {"message": "Item not found."}]
            
            return [204, {"message": f"Item deleted from {TABLE_NAME} successfully."}]

    except sqlite3.Error as e:
        return [500, {"error": str(e)}]


def find_item_by_id(id):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            # Set the row factory to sqlite3.Row - By setting conn.row_factory = sqlite3.Row, you tell SQLite to return rows as sqlite3.Row objects, which can be accessed like dictionaries.
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            cur.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = ?', (id,))
            data = cur.fetchall()
        
            if data:
                return [200, [dict(row) for row in data][0]]
            else:
                return [404, {"message": "Item not found"}]
        
    except sqlite3.Error as e:
        return [500, {"error": str(e)}]

#create_table()
#add_csv_to_db('international_names_with_rooms_1000.csv')