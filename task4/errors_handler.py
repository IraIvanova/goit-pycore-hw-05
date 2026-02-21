def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Name and phone are required."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."

    return inner