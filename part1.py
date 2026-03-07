with open('codingal.text', 'w') as file:
    file.write("Hi, I am Penguin and I am 1 yr old.")
file.close()

with open('codingal.text', 'r') as file:
    data = file.readlines()
    print("Words in this file are:")
    for line in data:
        word = line.split()
        print(word)

file.close()