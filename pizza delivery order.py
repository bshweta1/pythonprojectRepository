print("Welcome to python Pizza Deliveries!")

size = input("What size of pizza do you want? S, M or L: ")
Toppings = input("Which topping do you want on your pizza? capsicum, corn, black olive, mushroom, onion, tomato: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if Toppings in ["capsicum", "onion", "tomato"]:
    if size=="S":
       bill += 3
    else:
        bill+=5
elif Toppings == "corn":
    if size=="M":
        bill += 5
    else:
        bill+=6
else:
    if size=="L":
        bill += 7
    else:
        bill+=8

if extra_cheese == "Y":
    bill += 1

print(f"Final bill amount you have to pay: ${bill}")
