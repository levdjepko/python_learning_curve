# using the random module, do some coin flips
import random

count_heads = 0
count_tails = 0

for i in range(100):
    choice = random.randint(1, 2)
    if choice == 1:
        count_tails += 1
    else:
        count_heads += 1
print(f"Total heads: {count_heads}, tails: {count_tails}")
