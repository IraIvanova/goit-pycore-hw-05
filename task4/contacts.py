from errors_handler import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact changed."

@input_error
def show_phone(args, contacts):
    name = args[0]

    return contacts[name]

def show_all(contacts):
    if not contacts:
        return "No contacts saved."

    return "".join(f"{name}: {phone}\n" for name, phone in contacts.items())
