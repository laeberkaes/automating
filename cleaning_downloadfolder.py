import os
import shutil
import time
import getpass

user = getpass.getuser()
start_directory = "/home/" + str(user) + "/Downloads/"
pdf_directory = "/home/" + str(user) + "/Downloads/PDF"
iso_directory = "/home/" + str(user) + "/Downloads/ISO"
misc_directory = "/home/" + str(user) + "/Downloads/MISC"
fullpath = os.path.join

def main():
    while True:
        time.sleep(5)
        for dirname, dirnames, filenames in os.walk(start_directory):
            for filename in filenames:
                source = fullpath(dirname, filename)
                if filename.endswith("pdf"):
                    shutil.move(source, fullpath(pdf_directory, filename))
                elif filename.endswith("iso"):
                    shutil.move(source, fullpath(iso_directory, filename))
                else:
                    shutil.move(source, fullpath(misc_directory, filename))

if __name__ == '__main__':
    main()