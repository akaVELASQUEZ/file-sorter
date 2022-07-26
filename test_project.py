from project import folder, archive, error_check
import pytest

def main():

    test_error_check()
    test_proc()
    test_folder()
    test_archive()
    test_FileError()


# Test for value error on error_check function
def test_error_check():
    with pytest.raises(ValueError):
        error_check(2)
        error_check(cat)
        error_check(cs50)
        error_check(-1)

# Most Error handling is already in main function but functions also raises error for further checking
def test_FileError():
    with pytest.raises(FileExistsError):
        folder("NonExistentPath")
        archive("NonExistentPath")

def test_proc():
    assert error_check("0") == 0
    assert error_check("1") == 1

# Tests the folder function of project.py. Test folders should be changed to its initial state as running pytest
# would change the contents of the folder. Rerunning pytest without the initial test folders would cause the test to fail
def test_folder():
    assert folder("/workspaces/87757669/CS50P/project/test folders/test 1") == {"Images" : 1}
    assert folder("/workspaces/87757669/CS50P/project/test folders/test 2") == {"Images" : 1, "Sounds" : 1}
    assert folder("/workspaces/87757669/CS50P/project/test folders/test 3") == {"Images" : 2, "Sounds" : 1, "Documents" : 1, "Applications" : 1}

# Tests the archive function of project.py. Folders function should be called first to run the archive function.
# Test folders should be changed to its initial state as running pytest would change the contents of the folder.
# Rerunning pytest without the initial test folders would cause the test to fail
def test_archive():
    assert folder("/workspaces/87757669/CS50P/project/test folders/test 1 - Copy")
    assert archive("/workspaces/87757669/CS50P/project/test folders/test 1 - Copy", {"Images" : 1}) == 1

    assert folder("/workspaces/87757669/CS50P/project/test folders/test 2 - Copy")
    assert archive("/workspaces/87757669/CS50P/project/test folders/test 2 - Copy", {"Images" : 1, "Sounds" : 1}) == 2

    assert folder("/workspaces/87757669/CS50P/project/test folders/test 3 - Copy")
    assert archive("/workspaces/87757669/CS50P/project/test folders/test 3 - Copy", {"Images" : 2, "Sounds" : 1, "Documents" : 1, "Applications" : 1}) == 4

if __name__ == "__main__":
    main()