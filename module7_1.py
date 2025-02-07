def reverse_generator(iterable):
    for i in range(len(iterable) - 1, -1, -1):
        yield iterable[i]

test_list = [1, 2, 3, 4, 5]

for item in reverse_generator(test_list):
    print(item)
