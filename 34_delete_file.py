import os
import shutil

path = "34_test.txt"

try:
    os.remove(path) # delete file
    # shutil.rmtree(path) # remove a directory containing files
    # os.rmdir(path) # remove empty directory
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")
