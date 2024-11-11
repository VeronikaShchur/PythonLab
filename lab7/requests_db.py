import psycopg2
from datetime import date
from decimal import Decimal

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="clothing_store_db", user="user", password="password", host="localhost", port="5432"
)

with conn:
    cursor = conn.cursor()

    # 1. Відобразити інформацію по покупкам, відсортовано за назвою клієнта
    cursor.execute("""
        SELECT s.sale_date, p.product_name, c.client_name, s.quantity_sold, p.price
        FROM Sales s
        JOIN Products p ON s.product_id = p.product_id
        JOIN Clients c ON s.client_id = c.client_id
        ORDER BY c.client_name;
    """)
    purchases_info = cursor.fetchall()
    print("1) Інформація по покупкам (відсортовано за назвою клієнта):")
    for row in purchases_info:
        sale_date, product_name, client_name, quantity_sold, price = row
        print(", ".join(
            map(str, [sale_date.strftime("%Y-%m-%d"), product_name, client_name, quantity_sold, float(price)])))

    # 2. Відобразити увесь одяг за вибраним типом
    product_type = 'Жіночий'
    cursor.execute("""
        SELECT product_name, manufacturer, quantity_on_hand, price
        FROM Products
        WHERE product_type = %s;
    """, (product_type,))
    clothing_by_type = cursor.fetchall()
    print("\n2) Увесь одяг за вибраним типом (тип:", product_type, "):")
    for row in clothing_by_type:
        product_name, manufacturer, quantity_on_hand, price = row
        print(", ".join(map(str, [product_name, manufacturer, quantity_on_hand, float(price)])))

    # 3. Порахувати кількість покупок кожного клієнта
    cursor.execute("""
        SELECT c.client_name, COUNT(s.sale_id) AS purchases_count
        FROM Sales s
        JOIN Clients c ON s.client_id = c.client_id
        GROUP BY c.client_name;
    """)
    client_purchase_counts = cursor.fetchall()
    print("\n3) Кількість покупок кожного клієнта:")
    for row in client_purchase_counts:
        client_name, purchases_count = row
        print(", ".join(map(str, [client_name, purchases_count])))

    # 4. Порахувати вартість кожної покупки (без знижки та зі знижкою)
    cursor.execute("""
        SELECT s.sale_id, p.product_name, s.quantity_sold, 
               (p.price * s.quantity_sold) AS total_price,
               (p.price * s.quantity_sold * (1 - s.discount / 100)) AS discounted_price
        FROM Sales s
        JOIN Products p ON s.product_id = p.product_id;
    """)
    purchase_costs = cursor.fetchall()
    print("\n4) Вартість кожної покупки (без знижки та зі знижкою):")
    for row in purchase_costs:
        sale_id, product_name, quantity_sold, total_price, discounted_price = row
        print(", ".join(map(str, [sale_id, product_name, quantity_sold, float(total_price), float(discounted_price)])))

    # 5. Порахувати загальну суму витрат кожного клієнта
    cursor.execute("""
        SELECT c.client_name,
               SUM(p.price * s.quantity_sold * (1 - s.discount / 100)) AS total_spent
        FROM Sales s
        JOIN Clients c ON s.client_id = c.client_id
        JOIN Products p ON s.product_id = p.product_id
        GROUP BY c.client_name;
    """)
    total_spent_by_clients = cursor.fetchall()
    print("\n5) Загальна сума витрат кожного клієнта на купівлю одягу:")
    for row in total_spent_by_clients:
        client_name, total_spent = row
        print(", ".join(map(str, [client_name, float(total_spent)])))

    # 6. Відобразити кількість кожного виду одягу на кожному складі
    cursor.execute("""
        SELECT w.address, p.product_name, SUM(p.quantity_on_hand) AS total_quantity
        FROM Products p
        JOIN Warehouses w ON p.warehouse_id = w.warehouse_id
        GROUP BY w.address, p.product_name;
    """)
    stock_quantities = cursor.fetchall()
    print("\n6) Кількість кожного виду одягу на кожному складі:")
    for row in stock_quantities:
        address, product_name, total_quantity = row
        print(", ".join(map(str, [address, product_name, total_quantity])))

# Закриття з'єднання
conn.close()
