"""A coin flip program that returns the head or tail count
    """

from random import choice

print("Welcome to our coin flip game.")
num = input("How many times would you like to flip the coin?\n")
coin_sides = ["head", "tail"]
head_count: int = 0
tail_count: int = 0

for i in range(int(num)):
    side_shown = choice(coin_sides)
    if side_shown == "head":
        head_count += 1
    else:
        tail_count += 1
print(f"The flips had {head_count} heads and {tail_count} tails.")
print(f"The last side shown is {side_shown}")
