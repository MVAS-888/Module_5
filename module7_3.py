def prime_generator(n):
    count, num = 0, 2
    while count < n:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
            count += 1
        num += 1

print(list(prime_generator(10)))