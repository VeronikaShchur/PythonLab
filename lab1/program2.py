# Рекурсивна функція для генерації списку з n чисел Фібоначчі
def fibonacci_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_sequence(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

count = int(input("Введіть кількість чисел Фібоначчі: "))

# Виклик функції для отримання n чисел Фібоначчі
fibonacci_numbers = fibonacci_sequence(count)

print(f"{count} чисел Фібоначчі:")
print(" ".join(map(str, fibonacci_numbers)))
