import random 


number = random.randint(1,101)
print(number)
my_number = int(input("Enter a number"))

if my_number == number:
    print("You guessed my number")
else:
    print("You guess wrong my number is", number)

