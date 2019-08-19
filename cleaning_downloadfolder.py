import os
import shutil

start_directory = "/home/blackarch/Downloads/"
pdf_directory = "/home/blackarch/Downloads/PDF"
iso_directory = "/home/blackarch/Downloads/ISO"
misc_directory = "/home/blackarch/Downloads/MISC"
fullpath = os.path.join

# os.chdir("~/Downloads/")
def main():
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