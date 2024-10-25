import sqlite3
import csv

DB_NAME = 'room_type.db'
TABLE_NAME = "room_type"

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS room_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            low INTEGER,
            mid INTEGER,
            high INTEGER
        )
        """
        cur.execute(create_table_query)

def add_csv_to_db(filepath):
    with open(filepath, mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for line in csvFile:
            print(line)
            data = {
                "type": line[0] if line[0] else None,
                "low": int(line[1]) if line[1] else None,
                "mid": int(line[2]) if line[2] else None,
                "high": int(line[3]) if line[3] else None
            }
            add_new_item(data)
        return
    
def add_new_item(data):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()

            cur.execute(
                f'''
                INSERT OR IGNORE INTO {TABLE_NAME}
                (type, low, mid, high)
                VALUES (?,?,?,?)
                ''',
                (
                    data.get('type'),
                    data.get('low'),
                    data.get('mid'),
                    data.get('high')
                )
            )

            return [201, {"message": "New item added to database successfully."}] 
        
    except sqlite3.Erorr as e:
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
                        query += f'{key} ={value}'
                    else:
                        query += f'{key} = {value}'
                    i += 1

                query += f" WHERE id = {id}"
            print(query)

            cur.execute(query)
            if cur.rowcount == 0:
                return [404, {"message": "Room type not found."}]
            
            return [200, {"message": "Room type updated successfully."}]

    except sqlite3.Error as e:
        return [500, {"error": str(e)}]

def select_all_items():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM {TABLE_NAME}')

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
#add_csv_to_db('room_type.csv')