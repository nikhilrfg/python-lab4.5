user_input = input("Enter your age: ")

try:
    age = int(user_input)
    print("Success! Your age is: " + str(age))

except ValueError:
    print("Error: That is not a valid number!")