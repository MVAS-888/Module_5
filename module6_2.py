class MyList:
    def __init__(self, initial_data=None):
        self.data = initial_data or []

    def append(self, item):
        self.data.append(item)

    def clear(self):
        self.data.clear()

    def insert(self, index, value):
        self.data.insert(index, value)

    def pop(self):
        return self.data.pop() if self.data else None

    def remove_at(self, index):
        return self.data.pop(index) if 0 <= index < len(self.data) else None

    def __iter__(self):
        return iter(self.data)

    def __str__(self):
        return str(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(my_list)

my_list.append(6)
print(my_list)

my_list.insert(2, 10)
print(my_list)

my_list.pop()
print(my_list)

my_list.remove_at(1)
print(my_list)

my_list.clear()
print(my_list)