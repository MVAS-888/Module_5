class ReverseIterator:
    def __init__(self, iterable):
        self.data = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index -= 1
        return self.data[self.index]

test_list = [1, 2, 3, 4, 5]

for item in ReverseIterator(test_list):
    print(item)