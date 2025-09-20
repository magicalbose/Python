name = "robert" #String Data Type
age = 15 #Integer
is_student = True #Boolean
weight = 38.5 #Float

print("Name is:", name)
print("Data Type of Name is", type(name))
print("Age is:", age)
print("Data Type of Age is", type(age))
print()

print("Before Typecasting")
print("Date Type of Age is", type(age))
print()

print("After Typecasting")
age = str(age)
print(age)
print("Data Type of Age is", type(age))