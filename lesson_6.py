class Contact:
    def __init__(self, name, phone, job):
        self.name = name
        self.phone = phone
        self.job = job

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone}, job={self.job})"

    def get_info(self):
        return f"{self.name}, {self.phone}, {self.job}"


class UpdateContact(Contact):
    def __init__(self, name, phone, job, email):
        super().__init__(name, phone, job)
        self.email = email

    def __repr__(self):
        return f"UpdateContact(name={self.name}, phone={self.phone}, job={self.job}, email={self.email})"

    def get_email(self):
        return self.email

print("Methods in Contact class:")
contact_methods = [method for method in dir(Contact) if callable(getattr(Contact, method)) and not method.startswith("__")]
print(contact_methods)

print("\nMethods in UpdateContact class:")
update_contact_methods = [method for method in dir(UpdateContact) if callable(getattr(UpdateContact, method)) and not method.startswith("__")]
print(update_contact_methods)