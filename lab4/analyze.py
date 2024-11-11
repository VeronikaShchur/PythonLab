import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data, None
    except Exception as e:
        return None, f"Не вдалося відкрити файл: {e}"

def calculate_age(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except Exception as e:
        return None

def categorize_age(age):
    if age is None:
        return None
    elif age < 18:
        return 'до 18'
    elif 18 <= age <= 45:
        return '18-45'
    elif 45 < age <= 70:
        return '46-70'
    else:
        return 'старші 70'

def main():
    file_path = 'employees.csv'
    data, error = read_csv(file_path)

    if error:
        print(error)
        return
    else:
        print("Файл успішно відкрито!")

    if 'Стать' not in data.columns or 'Дата народження' not in data.columns:
        print("Невірний формат CSV файлу. Перевірте наявність колонок 'Стать' і 'Дата народження'!")
        return

    gender_counts = data['Стать'].value_counts()
    print("\nРозподіл співробітників по статі:")
    print(f"Чоловіків: {gender_counts.get('Чоловіча', 0)}")
    print(f"Жінок: {gender_counts.get('Жіноча', 0)}")

    plt.figure(figsize=(10, 6))
    gender_counts.plot(kind='bar', color=['#1f77b4', '#ff69b4'], edgecolor='black')  # Нові кольори
    plt.title('Розподіл співробітників по статі')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.show()

    data['Вік'] = data['Дата народження'].apply(calculate_age)

    if data['Вік'].isnull().any():
        print("Помилка обчислення віку. Перевірте правильність формату дати народження.")
        return

    age_categories = data['Вік'].apply(categorize_age).value_counts()
    print("\nКількість співробітників у кожній віковій категорії:")
    for category, count in age_categories.items():
        print(f"{category}: {count}")

    plt.figure(figsize=(10, 6))
    age_categories.plot(kind='bar', color=['#98fb98', '#ffcc99', '#ffa07a', '#20b2aa'], edgecolor='black')  # Нові кольори
    plt.title('Розподіл співробітників по вікових категоріях')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    gender_age_distribution = data.groupby(['Стать', data['Вік'].apply(categorize_age)]).size().unstack().fillna(0)
    print("\nРозподіл співробітників за статтю і віковими категоріями:")
    print(gender_age_distribution)

    gender_age_distribution.plot(kind='bar', figsize=(12, 8), edgecolor='black', color=['#1e90ff', '#ff69b4', '#32cd32', '#ffa07a'])  # Нові кольори
    plt.title('Розподіл співробітників по вікових категоріях та статі')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.legend(title='Вікова категорія')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
