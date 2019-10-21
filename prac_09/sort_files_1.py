import shutil
import os


def main():
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            # continue will finish the loop if it jumps to a dictionary
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        shutil.move(filename, '{}/{}'.format(extension, filename))


main()
