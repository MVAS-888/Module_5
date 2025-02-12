import primes

from primes import is_prime, get_primes

num = 29
if is_prime(num):
    print(f"{num} - це просте число!")
else:
    print(f"{num} - не просте число.")

limit = 50
primes_list = get_primes(limit)
print(f"Прості числа до {limit}: {primes_list}")
