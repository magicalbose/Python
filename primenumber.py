number = 39
flag = False

if number > 1:

    for i in range(2, number):

        if number % i == 0:
            flag = True
            break

elif number < 1:
    print("Please enter a number greater than 1.")


if flag:
    print(number, "is not a prime number.")

else:
    print(number, "is a prime number.")