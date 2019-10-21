import shutil
import os

EXTENSIONS = ['doc', 'docx', 'png', 'gif', 'txt', 'xls', 'xlsx', 'jpg']


def main():
    os.chdir('FilesToSort')
    for extension in EXTENSIONS:
        choice = input('What category would you like to sort {} files into?'.format(extension))
        try:
            os.mkdir(choice)
        except FileExistsError:
            pass

        for filename in os.listdir('.'):
            if os.path.isdir(filename):
                # continue will finish the loop if it jumps to a dictionary
                continue
            filename_extension = filename.split('.')[-1]
            if filename_extension == extension:
                shutil.move(filename, '{}/{}'.format(choice, filename))


main()
