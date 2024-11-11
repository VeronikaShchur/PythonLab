import pandas as pd
from datetime import datetime
import os

# Функція для обчислення віку
def get_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Функція для класифікації віку
def age_group(age):
    if age < 18:
        return 'до_18'
    elif 18 <= age <= 45:
        return '18-45'
    elif 46 <= age <= 70:
        return '45-70'
    else:
        return 'старше_70'

def convert_csv_to_xlsx(csv_file, xlsx_file):
    try:
        df = pd.read_csv(csv_file)

        required_columns = ["Прізвище", "Ім’я", "По батькові", "Дата народження"]
        if not all(column in df.columns for column in required_columns):
            raise ValueError("CSV файл не містить усіх необхідних колонок!")

        df['Дата народження'] = pd.to_datetime(df['Дата народження'], errors='coerce')
        df['Вік'] = df['Дата народження'].apply(lambda x: get_age(x) if pd.notnull(x) else None)

        age_categories = ['до_18', '18-45', '45-70', 'старше_70']
        categorized_dataframes = {category: df[df['Вік'].apply(lambda x: age_group(x) == category)] for category in age_categories}

        with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Усі записи', index=False)

            for category in age_categories:
                age_df = categorized_dataframes[category]
                age_df = age_df[['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']]
                age_df.index += 1
                age_df.index.name = '№'
                age_df.to_excel(writer, sheet_name=category, index=True)

        print("Файл XLSX успішно створено.")

    except FileNotFoundError:
        print("Помилка - CSV файл не знайдено або виникла проблема при його відкритті!")
    except Exception as e:
        print(f"Помилка при створенні XLSX файлу: {e}")

convert_csv_to_xlsx("employees.csv", "employees_groups.xlsx")
