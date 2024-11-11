import pandas as pd
import random
from faker import Faker
from datetime import datetime

faker_ua = Faker('uk_UA')

def create_birthdate():
    start_date = datetime(1938, 1, 1)
    end_date = datetime(2008, 12, 31)
    return faker_ua.date_between(start_date=start_date, end_date=end_date)

def assign_gender():
    return random.choices(["Чоловіча", "Жіноча"], [0.6, 0.4])[0]

def assign_job():
    return faker_ua.job()

def create_personal_record(gender):
    if gender == "Чоловіча":
        first_name = faker_ua.first_name_male()
        last_name = faker_ua.last_name_male()
        middle_name = faker_ua.middle_name_male()
    else:
        first_name = faker_ua.first_name_female()
        last_name = faker_ua.last_name_female()
        middle_name = faker_ua.middle_name_female()

    return {
        "Прізвище": last_name,
        "Ім’я": first_name,
        "По батькові": middle_name,
        "Стать": gender,
        "Дата народження": create_birthdate(),
        "Посада": assign_job(),
        "Місто проживання": faker_ua.city(),
        "Адреса проживання": faker_ua.address().replace("\n", ", "),
        "Телефон": faker_ua.phone_number(),
        "Email": faker_ua.email()
    }

def export_to_csv(filename, total_records):
    data_records = []

    male_records = int(total_records * 0.6)
    female_records = total_records - male_records

    for _ in range(male_records):
        data_records.append(create_personal_record("Чоловіча"))

    for _ in range(female_records):
        data_records.append(create_personal_record("Жіноча"))

    df = pd.DataFrame(data_records)
    df.to_csv(filename, index=False)

export_to_csv("employees.csv", 2000)
