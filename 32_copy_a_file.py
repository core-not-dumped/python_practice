# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
shutil.copyfile("31_test.txt", "32_test.txt") #src, dst
#shutil.copy("31_test.txt", "C:\\Users\\BroCode\\copy.txt") # destination can be other directory
#shutil.copy2("31_test.txt", "C:\\Users\\BroCode\\copy.txt")

