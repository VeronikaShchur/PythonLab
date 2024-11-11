import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="clothing_store_db", user="user", password="password", host="localhost", port="5432"
)

# Створення таблиць
with conn:
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Warehouses (
        warehouse_id SERIAL PRIMARY KEY,
        address VARCHAR(255),
        manager_name VARCHAR(100),
        phone VARCHAR(15)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        product_id SERIAL PRIMARY KEY,
        product_type VARCHAR(50) CHECK (product_type IN ('Жіночий', 'Чоловічий', 'Дитячий')),
        product_name VARCHAR(100),
        manufacturer VARCHAR(100),
        warehouse_id INTEGER REFERENCES Warehouses(warehouse_id),
        quantity_on_hand INTEGER,
        price NUMERIC(10, 2)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clients (
        client_id SERIAL PRIMARY KEY,
        client_name VARCHAR(100),
        client_address VARCHAR(255),
        phone VARCHAR(15),
        contact_person VARCHAR(100)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sales (
        sale_id SERIAL PRIMARY KEY,
        sale_date DATE,
        client_id INTEGER REFERENCES Clients(client_id),
        product_id INTEGER REFERENCES Products(product_id),
        quantity_sold INTEGER,
        discount NUMERIC(5, 2)
    );
    """)

    print("Таблиці успішно створено!")

# Заповнення таблиць даними
with conn:
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Warehouses (address, manager_name, phone)
    VALUES
    ('Вул. Хрещатик, 1, Київ', 'Іванов Іван', '+380661234567'),
    ('Вул. Пушкіна, 10, Львів', 'Петренко Олександр', '+380661234568'),
    ('Вул. Грушевського, 20, Одеса', 'Сидоренко Марія', '+380661234569');
    """)

    cursor.execute("""
    INSERT INTO Products (product_type, product_name, manufacturer, warehouse_id, quantity_on_hand, price)
    VALUES
    ('Жіночий', 'Сукня', 'Fashion Ltd', 1, 50, 1200.50),
    ('Чоловічий', 'Футболка', 'Trend Wear', 1, 150, 350.75),
    ('Дитячий', 'Штани', 'Kids Fashion', 2, 75, 500.25),
    ('Жіночий', 'Туфлі', 'Luxury Shoes', 3, 30, 1500.99),
    ('Чоловічий', 'Сорочка', 'Classic Wear', 1, 100, 700.45),
    ('Жіночий', 'Спідниця', 'Fashion Ltd', 2, 200, 800.30),
    ('Дитячий', 'Плаття', 'Cute Kids', 2, 120, 400.00),
    ('Чоловічий', 'Куртка', 'Winter Gear', 3, 45, 2500.99),
    ('Жіночий', 'Светр', 'Style Co.', 1, 70, 1100.60),
    ('Дитячий', 'Костюм', 'Kidswear Co', 1, 80, 750.50),
    ('Жіночий', 'Шорти', 'Summer Style', 2, 90, 650.20),
    ('Чоловічий', 'Джинси', 'Denim Works', 3, 55, 1300.40),
    ('Жіночий', 'Блуза', 'Chic Wear', 1, 120, 950.60),
    ('Чоловічий', 'Спортивний костюм', 'Sport Fashion', 2, 60, 1500.99),
    ('Дитячий', 'Шапка', 'Cute Kids', 3, 150, 300.00);
    """)

    cursor.execute("""
    INSERT INTO Clients (client_name, client_address, phone, contact_person)
    VALUES
    ('Петро Петров', 'вул. Лесі Українки, 5, Київ', '+380661234570', 'Петро Петров'),
    ('Марія Іванова', 'вул. Сумська, 15, Харків', '+380661234571', 'Марія Іванова'),
    ('Олександр Семенов', 'вул. Б. Хмельницького, 12, Львів', '+380661234572', 'Олександр Семенов'),
    ('Наталія Дорошенко', 'вул. Академіка Сахарова, 22, Одеса', '+380661234573', 'Наталія Дорошенко'),
    ('Іван Коваленко', 'вул. Петра Кучеренка, 8, Дніпро', '+380661234574', 'Іван Коваленко');
    """)

    cursor.execute("""
    INSERT INTO Sales (sale_date, client_id, product_id, quantity_sold, discount)
    VALUES
    ('2024-11-01', 1, 1, 2, 5.00),
    ('2024-11-02', 2, 3, 1, 10.00),
    ('2024-11-03', 3, 2, 5, 0.00),
    ('2024-11-04', 4, 5, 3, 7.50),
    ('2024-11-05', 5, 4, 1, 0.00),
    ('2024-11-06', 1, 6, 2, 5.00),
    ('2024-11-07', 2, 8, 4, 15.00),
    ('2024-11-08', 3, 10, 1, 5.00),
    ('2024-11-09', 4, 9, 3, 10.00),
    ('2024-11-10', 5, 12, 2, 0.00);
    """)

    print("Таблиці успішно заповнено даними!")

# Закриття з'єднання
conn.close()
