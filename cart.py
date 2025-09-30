print("Welcome to our grocery")

groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

cart = {}

while True:
    user_input = input("What do you want to buy? (type 'item quantity' or 'done' to finish): ")

    if user_input == "done":
        break

    parts = user_input.split()

    if len(parts) == 0:
        continue

    item = parts[0]

    amount = 1

    if len(parts) == 2 and parts[1].isdigit():
        amount = int(parts[1])
    elif len(parts) == 2 and not parts[1].isdigit():
        print("Invalid quantity. Please enter a number after the item.")
        continue

    if item in groceries:
        if item in cart:
            cart[item] += amount
        else:
            cart[item] = amount
    else:
        print("Sorry, we don’t have that item.")

total = 0

for item, amount in cart.items():
    price = groceries[item]
    total += price * amount

 

print("\nYou bought:")
for item, amount in cart.items():
    print(f"- {item}: {amount}")

print("Total = $", total)


if "milk" in cart and cart["milk"] > 2:
    print("Since you bought more than 2 milk, you get a $1 discount on your total.")
    total -= 1 
if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")
