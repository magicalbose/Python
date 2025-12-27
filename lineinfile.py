file = open("codingal.txt","r")
Counter = 0

Content = file.read()

lines = Content.split("\n")

for i in lines:
    if i:
        Counter = Counter + 1

print("This is the number of lines in the file: ")
print(Counter)