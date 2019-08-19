def main():
    password = input("Pick a Password: ")
    while len(password) < 6:
        print("Password not long enough")
        password = input("Pick another Password: ")
    print('*' * len(password))

main()