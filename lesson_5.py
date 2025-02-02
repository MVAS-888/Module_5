class Contact:
    def __init__(self, name, phone, job):
        self.name = name
        self.phone = phone
        self.job = job

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone}, job={self.job})"


class UpdateContact(Contact):
    def __init__(self, name, phone, job, email):
        super().__init__(name, phone, job)
        self.email = email

    def __repr__(self):
        return f"UpdateContact(name={self.name}, phone={self.phone}, job={self.job}, email={self.email})"

contact1 = Contact("Dan Don", "123-456-7890", "Engineer")
contact2 = UpdateContact("Koka Smith", "098-765-4321", "Designer", "jane.smith@example.com")

print("Before deleting 'job' attribute:")
print(contact1)
print(contact2)

del contact1.job
del contact2.job

print("\nAfter deleting 'job' attribute:")
print(contact1.__dict__)
print(contact2.__dict__)
