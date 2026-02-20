import contacts as contacts_helper

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *[arg.strip() for arg in args]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(contacts_helper.add_contact(args, contacts))
        elif command == "change":
            print(contacts_helper.change_contact(args, contacts))
        elif command == "phone":
            if not args:
                print("Please, provide a contact name.")
            else:
                print(contacts_helper.show_phone(args[0], contacts))
        elif command == "all":
            print(contacts_helper.show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()