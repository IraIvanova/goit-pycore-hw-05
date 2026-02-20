def add_contact(args, contacts):
    if len(args) < 2:
        return "Please, provide both name and phone number."

    name, phone = args
    contacts[name] = phone

    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Please, provide both name and phone number."

    name, phone = args

    if not check_if_contact_exists(name, contacts):
        return "Contact not found."

    contacts[name] = phone
    return "Contact changed."

def show_phone(name, contacts):
    if not check_if_contact_exists(name, contacts):
        return "Contact not found."

    return contacts[name]

def show_all(contacts):
    if not contacts:
        return "No contacts saved."

    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result


def check_if_contact_exists(name, contacts):
    return name in contacts