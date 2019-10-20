"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def demo_walk():
    """Process all subdirectories using os.walk()."""
    # os.chdir('Lyrics')
    # for directory_name, subdirectories, filenames in os.walk('.'):
    #     print("Directory:", directory_name)
    #     print("\tcontains subdirectories:", subdirectories)
    #     print("\tand files:", filenames)
    #     print("(Current working directory is: {})".format(os.getcwd()))
    #     for filename in filenames:
    #         full_name = os.path.join(directory_name, filename)
    #         new_name = os.path.join(directory_name, get_fixed_filename(filename))
    #         os.rename(full_name, new_name)
    filename = 'ItIsWell (oh my soul).txt'
    get_fixed_filename(filename)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    new_filename = ''
    number_of_splits = 0
    for i, element in enumerate(filename):
        if i == (len(filename) - 1-number_of_splits):
            pass
        elif element == ' ' and filename[i+1+number_of_splits].islower():
            filename = filename[:i+1+number_of_splits] + filename[i+1+number_of_splits].upper() + filename[i+2+number_of_splits:]
        elif element == "(" and filename[i+1+number_of_splits].islower():
            filename = filename[:i+1+number_of_splits] + filename[i+1+number_of_splits].upper() + filename[i+2+number_of_splits:]
        elif element.islower() and filename[i + 1+number_of_splits].isupper():
            filename = filename[:i + 1+number_of_splits] + ' ' + filename[i+1+number_of_splits:]
            number_of_splits +=1

    if new_filename == '':
        new_filename = filename
    new_name = new_filename.replace(" ", "_").replace(".TXT", ".txt")
    print(new_name)

# main()
demo_walk()
