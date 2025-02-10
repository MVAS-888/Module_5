#Завдання 1
#Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
#Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.

import random

with open("random_numbers.txt", "w") as file:
    for _ in range(10000):
        file.write(f"{random.uniform(0, 1000)}\n")

print("10,000 random numbers saved to random_numbers.txt")


with open("random_numbers.txt", "r") as file:
    numbers = map(float, file.readlines())

print(f"Sum of numbers: {sum(numbers)}")

