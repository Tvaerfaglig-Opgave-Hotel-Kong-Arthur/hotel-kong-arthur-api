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
        df.to_sql ("drinks", con=engine, if_exists="replace", index=False)

        print("Data imported succesfully into 'drinks' table")

    except Exception as e:
        print(f"An error occurred: {e}")


#create_table()
#add_excel_to_db()