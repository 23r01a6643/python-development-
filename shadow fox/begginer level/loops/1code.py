import random
count_6 = 0
count_1 = 0
count_double_6 = 0
previous_roll = None
for i in range(20):
    roll = random.randint(1, 6)
    if roll == 6:
        count_6 += 1
    elif roll == 1:
        count_1 += 1
    if roll == 6 and previous_roll == 6:
        count_double_6 += 1
    previous_roll = roll
print(f"Times rolled a 6: {count_6}")
print(f"Times rolled a 1: {count_1}")
print(f"Times rolled two 6s in a row: {count_double_6}")
