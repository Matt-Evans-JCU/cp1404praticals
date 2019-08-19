def main():
    password = get_password()
    print(print_password(password))


def get_password():
    password_choice = input("Pick a Password: ")
    while len(password_choice) < 6:
        print("Password not long enough")
        password_choice = input("Pick another Password: ")
    return password_choice


def print_password(password):
    return '*' * len(password)


main()
