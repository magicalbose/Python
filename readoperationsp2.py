#opening a file with one line
file = open('codingal.txt', 'r')
print("Reading first line: ")
print(file.readline())
file.close()

#opening a file with multiple lines
file = open('codingal.txt', 'r')
print("Reading multiple lines: ")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#opening a file with loops
file = open('codingal.txt', 'r')
print("Looping through the lines: ")
for line in file:
    print(line)
file.close()