class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"{self.name} {self.surname}, {self.age} років, Телефон: {self.mob_phone}, Email: {self.email}"

    def send_message(self, message):
        return f"Надсилання повідомлення '{message}' на {self.mob_phone}" 

class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"{self.name} {self.surname} працює як {self.job}" 

contact1 = Contact("Іванов", "Іван", 30, "+380501234567", "ivanov@example.com")
update_contact1 = UpdateContact("Петров", "Петро", 35, "+380671234567", "petrov@example.com", "Інженер")

print("Словник атрибутів contact1:", contact1.__dict__)
print("Словник атрибутів update_contact1:", update_contact1.__dict__)
print("Базовий клас UpdateContact:", UpdateContact.__base__)
print("Усі базові класи UpdateContact:", UpdateContact.__bases__)

attributes = ["surname", "name", "age", "mob_phone", "email", "job"]

for attr in attributes:
    print(f"Перевірка існування {attr} в update_contact1:", hasattr(update_contact1, attr))
    if hasattr(update_contact1, attr):
        print(f"Значення {attr} в update_contact1:", getattr(update_contact1, attr))
        setattr(update_contact1, attr, "Змінене значення")
        print(f"Нове значення {attr} в update_contact1:", getattr(update_contact1, attr))

        if attr == "job":
            delattr(update_contact1, attr)
            print(f"Після видалення {attr} в update_contact1:", hasattr(update_contact1, attr))

print(contact1.get_contact())
print(update_contact1.get_contact())