
print("Welcome to our grocery")


groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}
 
cart = []

while True:
    item = input("What do you want to buy? ")

    if item == "done":
        break

    if item in groceries:
        cart.append(item)

    else:
        print("Sorry, we don’t have that item.")

print("You bought:", cart)

total = 0
for item in cart:
    total += groceries[item]

print("You bought:", cart)
print("Total = $", total)


if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")