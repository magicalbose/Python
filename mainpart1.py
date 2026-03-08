with open('code.txt', 'w') as file:
    file.write("I love to code everyday!")
file.close()

with open('code.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file:")
    for line in data:
        word = line.split()
        print(word)

file.close()