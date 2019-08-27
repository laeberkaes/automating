import os
import shutil
import time
import getpass

user = getpass.getuser()
start_directory = "/home/" + str(user) + "/Downloads/"
pdf_directory = "/home/" + str(user) + "/Downloads/PDF"
iso_directory = "/home/" + str(user) + "/Downloads/ISO"
misc_directory = "/home/" + str(user) + "/Downloads/MISC"
picture_directory = "/home/" + str(user) + "/Downloads/PIC"
text_directory = "/home/" + str(user) + "/Downloads/TXT"
zip_directory = "/home/" + str(user) + "/Downloads/ZIP"
fullpath = os.path.join

def main():
    while True:
        time.sleep(5)
        for dirname, dirnames, filenames in os.walk(start_directory):
            for filename in filenames:
                source = fullpath(dirname, filename)
                if filename.endswith("pdf"):
                    shutil.move(source, fullpath(pdf_directory, filename))
                elif filename.endswith("iso") or filename.endswith("img"):
                    shutil.move(source, fullpath(iso_directory, filename
                    shutil.move(source, fullpath(picture_directory, filename))
                elif filename.endswith("txt"):
                    shutil.move(source, fullpath(text_directory, filename))
                elif filename.endswith("zip") or filename.endswith("xz") or filename.endswith("tgz"):
                    shutil.move(source, fullpath(zip_directory, filename))
                else:))
                elif filename.endswith("jpg") or filename.endswith("png"):
                    shutil.move(source, fullpath(misc_directory, filename))

if __name__ == '__main__':
    main()