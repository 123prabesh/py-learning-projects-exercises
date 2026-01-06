menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 2.50,
    "fries": 2.50,
    "chips": 1.00,
    "soda": 3.50,
    "lemonade": 4.25
}


cart = []
total = 0

print("------------- MEMU -------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("What would you like to order (q to quit):")

while True:
   food = input("").lower()

   if food == "q":
       break
   elif food not in menu.keys():
       print("Item doesnt exist.")
   else:
       cart.append(food)
print(f"{'Items':10} Price($)")
print("-"*15)
for food in cart:
    print(f"{food:10}: ${menu.get(food)}")
for food in cart:
    total = total + menu.get(food)
print("-"*15)
print(f"\033[31mThe total amount is {total:.2f}.\033[0m")