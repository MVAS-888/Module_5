def even_squares_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num ** 2

numbers = [1, 2, 3, 4, 5, 6]
print(list(even_squares_generator(numbers)))

# 2 варіант 
numbers = [1, 2, 3, 4, 5, 6]
squares = []

for num in numbers:
    if num % 2 == 0:
        squares.append(num ** 2)

print(squares)

