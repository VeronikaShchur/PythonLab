# Функція для перевірки, чи є число простим
def is_simple_number(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for divisor in range(3, int(num**0.5) + 1, 2):
        if num % divisor == 0:
            return False
    return True

first_num = int(input("Введіть перше число: "))
second_num = int(input("Введіть друге число: "))

lower_bound = min(first_num, second_num)
upper_bound = max(first_num, second_num)

# Збір всіх простих чисел у списку
prime_numbers = [number for number in range(lower_bound, upper_bound + 1) if is_simple_number(number)]

print(f"Прості числа в інтервалі [{lower_bound}, {upper_bound}]:")
print(" ".join(map(str, prime_numbers)))
