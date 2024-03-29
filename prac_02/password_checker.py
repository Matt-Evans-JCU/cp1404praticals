"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < 2 or len(password) > 6:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    #for i in range(0,len(password)):
    for character in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if character.isdigit():
            count_digit += 1
        elif character.islower():
            count_lower += 1
        elif character.isupper():
            count_upper += 1
        elif character in SPECIAL_CHARACTERS:
            count_special += 1
    # TODO: if any of the 'normal' counts are zero, return False, Can also use or to make neater
    if count_lower == 0:
        return False
    elif count_upper == 0:
        return False
    elif count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            # TODO: if special characters are required, then check the count of those
            return False
    return True


main()