# File Sorter
#### Video Demo:  <https://youtu.be/bSdmAJHHxW4>
#### Description: Sorts directory contents based on its file type. Could be moved to a directory or archived to a zip file
#


# Introduction
Good day everyone, I'm Allan Kristoffer Velasquez, an electrical engineer from Philippines.
My project **File Sorter** is something I want to do as a project for CS50x before but Im not sure how to implement it that time that's why I sticked to another project idea I have. But thanks to introduction to File I/O on this course as well as other python courses I took, I now have the capability to make this project.
File sorter is a program that sorts file contents based on its file type. A solution for messy directories that is too much of a pain to manually sort. This program supports 2 procedures, you could move your files through directories or through archives.


# Code Structure
File Sorter is a python program with 3 functions named folder, archive and error_check. Test_project.py is for pytest or function testing that consist of 5 tests that checks the operation of the 3 functions of project and error inducing inputs.

## Main function
The **Main Function** handles the collection of input from the user, printing instuctions and summary of results of the functions in it. This is also where the error handling and the conditional statement of which function to call based on procedure input of the user.

## Error_check Function
A simple function that checks the procedure input of the user. On my trials on testing my projecy, I noticed that value error could only be raised when the inputs for path and procedure is submitted. This function is made to solve the problem by instantly raising value error even without the path input.

## Folder Function
The function that sorts the files on the given path directory. Once the path is validated, a list of content would be created using os.listdir. Then, a for loop would be used to iterate to each item of the list. The function would then check the file extension of the content and would move(using shutil.move) it to a directory based on its file type. A counter is also created to count how many files is moved in the directory. After sorting the directory, this function would return the counts of the file moved in the sort directories in a dictionary format.

## Archive Function
This function takes 2 arguments, the path from the user and the count directory returned by the folder function. The directory would be used to decide how many archived would be made. This function would iterate on the key values of the dictionary, that also means the number of sort directories made by the folder function. By using shutil.make_archive, the function would make an archive for each key of the dictionary. Then, it would delete the directory and its content using shutil.rmtree. This function would return the number of archived made by the function.

## Test_project.py
Used for testing the functions of project.py. Listed are the tests in the program.
- test_error_check() = Used to check the if the program would raise value error on invalid procedure input.
- test_proc() = Used to check the error_check function of project.py.
- test_folder() = Used to check the folder function of project.py.
- test_archive() = Used to check the archive function of project.py.
- test_FileError() = Used to check the if the program would raise FileExistsError on non existent paths.