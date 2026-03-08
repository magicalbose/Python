new_file = open("NewFile.txt", 'x')
new_file.close()

import os
print("Does this file exist:")

if os.path.exists("my.file.txt"):
    os.remove("my.file.txt")
else:
    print("No, this file doesn't exist.")

my_files = open('my_files.txt', 'w')
my_files.write("I am student of Codingal.")

os.remove('codingal.txt')