import os
from os import path
import shutil
import sys

def main():

    # Prompts the user until the user exits the program
    while True:
        try:

            # Prints the header and instructions to the user
            print("--------------------------------------------------")
            print("Welcome to File Sorter")
            print("How would you like to sort your files?")
            print("0 : Folders (Move the files into folders)")
            print("1 : Archive (Archive the files into ZIP Files)")
            print("or exit to quit the program")

            # Gets input from the user. Raise errors if necessary. Exits the program when exit is submitted
            proc = input("Procedure: ")

            # Checks for ValueErrors on the procedure input
            proc = error_check(proc)

            proc = int(proc)

            add = input("Path of the folder: ")

            if not path.exists(add):
                raise FileExistsError

            # Based on the procedure type from user. Sorts the file using either folders or archives
            if proc == 0:
                counts = folder(add)

                # Prints the number of files moved on each folder
                for key in counts:
                    print(f"{counts[key]} files have been moved to {key} folder")

            # Make use of the folder function used in folder procedure to sort the files in folder
            # Calls the archive function to create a zip files using the folders from folder function
            elif proc == 1:
                counts = folder(add)
                count = archive(add, counts)

                # Prints the number of files moved on each folder and the count of archives created
                for key in counts:
                    print(f"{counts[key]} files have been archived to {key}.zip")

                print(f"{count} number of zip files created")

            else:
                raise ValueError

        # Error handling if the input is not 0, 1 or exit or if path does not exist
        except ValueError:
            print("Invalid Input")

        except FileExistsError:
            print("File Error")


# Checks for Value Errors on the input
def error_check(proc):

    proc = str(proc)
    
    # Exits the program if submitted exit
    if proc.lower() == 'exit':
        sys.exit("Quitting Program")

    # Raise ValueError if the input is not an integer or not equals to 0 or 1
    proc = int(proc)

    if proc < 0 or proc > 1:
        raise ValueError

    # Returns proc after error checks
    return proc



def folder(add):

    # Raise error if file path does not exist
    if not path.exists(add):
        raise FileExistsError

    # Gets the list of contents on the given path
    contents = os.listdir(add)

    # Tupples for checking the extension of the file
    img = (".gif", ".jpg", ".jpg", ".png", ".bmp")
    vid = (".mp4", ".mov", ".wmv", ".flv", ".avi", ".mkv" ".wmv")
    doc = (".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".html", ".htm" ".ods" ".odt", ".csv")
    arc = (".rar", ".zip", ".7z", ".zipx", ".tar")
    app = (".exe", ".apk", ".ipa", ".run", ".app", ".x86", ".scr", ".jar", ".py")
    music = (".mp3", ".wav", ".flac", ".alac", ".aac", ".ogg", ",ogx", ".midi")

    # Initialize a counter for files moved in each folder
    counts = {}

    # Loops each item in the list of contents in the path
    for item in contents:

        # Checks if the item is a file or not
        if path.isfile(add + "/" + item):

            # If it's a file, checks the file extension of the file.
            if item.lower().endswith(img):

                # If the file is an image, this commands would run. Creates an Images folder if it does not exists
                # and move the file to the said directory. Will simply move the file if the Images folder exists already
                if path.exists(add + "/Images"):
                    shutil.move(add + "/" + item, add + "/Images" + "/" + item )

                else:
                    os.mkdir(add + "/Images")
                    shutil.move(add + "/" + item, add + "/Images" + "/" + item )

                # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
                if "Images" in counts:
                    counts["Images"] += 1

                else:
                    counts["Images"] = 1

            elif item.lower().endswith(vid):

                # If the file is a video, this commands would run. Creates an Videos folder if it does not exists
                # and move the file to the said directory. Will simply move the file if the Videos folder exists already
                if path.exists(add + "/Videos"):
                    shutil.move(add + "/" + item, add + "/Videos" + "/" + item )

                else:
                    os.mkdir(add + "/Videos")
                    shutil.move(add + "/" + item, add + "/Videos" + "/" + item )

                # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
                if "Videos" in counts:
                    counts["Videos"] += 1

                else:
                    counts["Videos"] = 1

            elif item.lower().endswith(doc):

                # If the file is a document, this commands would run. Creates an Documents folder if it does not exists
                # and move the file to the said directory. Will simply move the file if the Documents folder exists already
                if path.exists(add + "/Documents"):
                    shutil.move(add + "/" + item, add + "/Documents" + "/" + item )

                else:
                    os.mkdir(add + "/Documents")
                    shutil.move(add + "/" + item, add + "/Documents" + "/" + item )

                # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
                if "Documents" in counts:
                    counts["Documents"] += 1

                else:
                    counts["Documents"] = 1

            elif item.lower().endswith(arc):

                # If the file is an archive, this commands would run. Creates an Archives folder if it does not exists
                # and move the file to the said directory. Will simply move the file if the Archives folder exists already
                if path.exists(add + "/Archives"):
                    shutil.move(add + "/" + item, add + "/Archives" + "/" + item )

                else:
                    os.mkdir(add + "/Archives")
                    shutil.move(add + "/" + item, add + "/Archives" + "/" + item )

                # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
                if "Archives" in counts:
                    counts["Archives"] += 1

                else:
                    counts["Archives"] = 1

            elif item.lower().endswith(app):

                # If the file is an application, this commands would run. Creates an Applications folder if it does not exists
                # and move the file to the said directory. Will simply move the file if the Applications folder exists already
                if path.exists(add + "/Applications"):
                    shutil.move(add + "/" + item, add + "/Applications" + "/" + item )

                else:
                    os.mkdir(add + "/Applications")
                    shutil.move(add + "/" + item, add + "/Applications" + "/" + item )

                # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
                if "Applications" in counts:
                    counts["Applications"] += 1

                else:
                    counts["Applications"] = 1

            elif item.lower().endswith(music):

                # If the file is a music, this commands would run. Creates an SOunds folder if it does not exists
                # and move the file to the said directory. Will simply move the file if the Sounds folder exists already
                if path.exists(add + "/Sounds"):
                    shutil.move(add + "/" + item, add + "/Sounds" + "/" + item )

                else:
                    os.mkdir(add + "/Sounds")
                    shutil.move(add + "/" + item, add + "/Sounds" + "/" + item )

                # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
                if "Sounds" in counts:
                    counts["Sounds"] += 1

                else:
                    counts["Sounds"] = 1
            else:

                # If the file type not listed above, this commands would run. Creates an Others folder if it does not exists
                # and move the file to the said directory. Will simply move the file if the Others folder exists already
                if path.exists(add + "/Others"):
                    shutil.move(add + "/" + item, add + "/Others" + "/" + item )

                else:
                    os.mkdir(add + "/Others")
                    shutil.move(add + "/" + item, add + "/Others" + "/" + item )

                # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
                if "Others" in counts:
                    counts["Others"] += 1

                else:
                    counts["Others"] = 1

        elif path.isdir(add + "/" + item):

            # If the item is a folder, this commands would run. Creates an Folders folder if it does not exists
            # and move the file to the said directory. Will simply move the file if the Folders folder exists already
            if path.exists(add + "/Folders"):
                shutil.move(add + "/" + item, add + "/Folders" + "/" + item )

            else:
                os.mkdir(add + "/Folders")
                shutil.move(add + "/" + item, add + "/Folders" + "/" + item )

            # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
            if "Folders" in counts:
                counts["Folders"] += 1

            else:
                counts["Folders"] = 1

        else:

            # If the item is not identified as file or folder, this commands would run. Creates an Videos folder if it does not exists
            # and move the file to the said directory. Will simply move the file if the Videos folder exists already
            if path.exists(add + "/Others"):
                shutil.move(add + "/" + item, add + "/Others" + "/" + item )

            else:
                os.mkdir(add + "/Others")
                shutil.move(add + "/" + item, add + "/Others" + "/" + item )

            # Creates a key:value pair in the counts dictionary if it does not exists, adds 1 to the counter if it exist
            if "Others" in counts:
                counts["Others"] += 1

            else:
                counts["Others"] = 1

    # Returns the dictionary counts
    return counts


def archive(add, counts):

    # Raise error if file path does not exist
    if not path.exists(add):
        raise FileExistsError

    # Initialize a counter to count number of archive created
    count = 0

    # Creates an archive based on the number of folders created by folder
    for key in counts:

        # Checks again if the directory exists
        if path.exists(add + "/" + key):

            # Creates an archive using the files inside the key folder and delete the folder with its content
            # Adds 1 to the counter for each archived created
            shutil.make_archive(add + "/" + key, "zip", add + "/" + key)
            shutil.rmtree(add + "/" + key)
            count += 1

    # Return the number of archived created
    return count


if __name__ == "__main__":
    main()