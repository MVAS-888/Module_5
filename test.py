import random

def random_number_generator(number_of_numbers):
  for _ in range(number_of_numbers):
    yield random.randint(0, 100)

result = [number * 2 for number in random_number_generator(10)]

print(result)