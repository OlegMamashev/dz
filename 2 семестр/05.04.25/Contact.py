from typing import Protocol


class Contact():
    all_contacts: list["Contact"] = []

    def __init__(self, name: str, email: str, *args) -> None:
        self.name = name
        self.email = email
        super().__init__(*args)
        Contact.all_contacts.append(self)


    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )
    

class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we woulf send "
            f"'{order}' order to '{self.name}'"
        )


class ContactList(list[Contact]):
    def search(self, name: str) -> list[Contact]:
        matching_contacts: list[Contact] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class AdressHolder():
    def __init__(self, street: str, city: str, state: str, code: str, *args):
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        super().__init__(*args)


class Friend(Contact, AdressHolder):
    def __init__(
            self, 
            name: str, 
            email: str, 
            phone: str,
            *args
            ) -> None:
        super().__init__(*args)
        AdressHolder.__init__(self, street, city, state, code)
        self.phone = phone


class Emailable(Protocol):
    email: str


class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email=}") 


class EmailableContact(Contact, MailSender):
    pass


class Nameble(Protocol):
    name: str


class NameSender(Nameble):
    def send_nmae(self, messege: str) -> None:
        print(f"send messege to {self.name}: {messege}")


class NamebleContact(Contact, NameSender):
    pass


# Contact('Mike', 'mike1@example.com')
# Contact('Mike', 'mike@example.com')
# Contact('Mike', 'mike@example.com')
# Contact('Mike', 'mike@example.com')
# Contact('Mike', 'mike2@example.com')
# a = Contact('1', '1')
# s = Supplier('Test', 'test@example.com')
# s1 = Supplier('1234', '213123123123@mail.ru')

# a = ContactList.search(Contact.all_contacts, 'Test')
j = Friend('Nsef', 
'12323',
'123123',
'123123123',
'12312123',
'123123',
'123213123',
'12',
'123123')
