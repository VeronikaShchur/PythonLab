import psycopg2
from prettytable import PrettyTable


def print_table_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]

    table = PrettyTable()
    table.field_names = colnames
    for row in rows:
        table.add_row(row)

    print(f"\nTable: {table_name}")
    print(table)


# Функція для виведення структури всіх таблиць та їхніх даних
def show_all_tables_data(cursor, tables):
    for table in tables:
        print_table_data(cursor, table)


# Підключення до бази даних
conn = psycopg2.connect(
    dbname="clothing_store_db", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

# Список таблиць
tables = ['Warehouses', 'Products', 'Clients', 'Sales']

# Виведення даних з усіх таблиць
show_all_tables_data(cursor, tables)

# Закриття з'єднання
cursor.close()
conn.close()
