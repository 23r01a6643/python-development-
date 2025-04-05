total_jumping_jacks = 0
for i in range(10): 
    total_jumping_jacks += 10
    print(f"You've completed {total_jumping_jacks} jumping jacks.")
    tired = input("Are you tired? (yes/no): ").lower()
    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip == "yes" or skip == "y":
            print(f"You completed a total of {total_jumping_jacks} jumping jacks.")
            break
    else:
        remaining = 100 - total_jumping_jacks
        if remaining > 0:
            print(f"{remaining} jumping jacks remaining.")
        else:
            print("Congratulations! You completed the workout.")
            break
