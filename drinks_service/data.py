import sqlite3
import pandas as pd
from sqlalchemy import create_engine

DB_NAME = 'drinks.db'
TABLE_NAME = 'drinks'

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            drink_name TEXT,
            category TEXT,
            price INTEGER,
            units_sold INTEGER,
            UNIQUE(drink_name, category)
        )
        """
        
        # Execute the create table statement
        cur.execute(create_table_query)

def add_excel_to_db ():
    try:
        # Load the excel file into pandas dataframe
        df = pd.read_excel("drinks_menu_with_sales.xlsx", sheet_name="Sheet1", header=0)

        print("DataFrame Loaded:")
        print(df.head()) 

        # create an sqlite database connection 
        engine = create_engine("sqlite:///drinks.db")

        # write the dataframe to the sqlite table
        df.to_sql ("drinks", con=engine, if_exists="append", index=False)

        print("Data imported succesfully into 'drinks' table")

    except Exception as e:
        print(f"An error occurred: {e}")

def select_all_drinks ():
    try:
        with sqlite3.connect(DB_NAME) as conn: 
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            cur.execute(f'SELECT * FROM {TABLE_NAME}')
            data = cur.fetchall()

            if data:
                return [200, [dict(row) for row in data] ]
            else:
                return [204, {"message": f"No items in {TABLE_NAME}"}]
        
    except sqlite3.Error as e:
        return [500, {"error": str(e)}]

def drinks_category (category : str):
    try:
        with sqlite3.connect(DB_NAME) as conn: 
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            cur.execute(f'SELECT drink_name, category FROM {TABLE_NAME} WHERE category = "{category}"')
            data = cur.fetchall()

            if data:
                drinks = [dict(row) for row in data]
                return [200, drinks]
            else:
                return [204, {"message": f"No items in {TABLE_NAME}"}]
        
    except sqlite3.Error as e:
        return [500, {"error": str(e)}]

#create_table()
#add_excel_to_db()