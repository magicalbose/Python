#opening a file in read mode
file = open('codingal.txt', 'r')
print(file.read())
file.close()

#opening a file in parts (characters)
file = open('codingal.txt', 'r')
print("\n Read in parts:")
print(file.read(8))
file.close()

#opening a file in append mode
file = open('codingal.txt', 'a')
file.write("Hi, I am Stuart and I am 15 years old.")
file.close()