input()

input("What is your name?: ")

name = input("What is your name?: ")
print("Hello " + name)

name = input("What is your name?: ")
age = input("What is your age?: ")
# age = age + 1 will not work, as input is detected as string
print(age)

age = int(input("Age?: "))
age = age + 1
print(str(age))
