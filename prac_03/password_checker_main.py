MIN_LENGTH = 6

def main():
    password = get_password()
    print(generate_asterisk(password))


def get_password():
    password_choice = input("Pick a Password: ")
    while len(password_choice) < MIN_LENGTH:
        print("Password not long enough")
        password_choice = input("Pick another Password: ")
    return password_choice


def generate_asterisk(password):
    return '*' * len(password)


main()
