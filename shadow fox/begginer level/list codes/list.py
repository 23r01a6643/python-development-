#Final code(performs all statements):
# Initial list of Justice League members
justice_league = ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', ['Batgirl', 'Nightwing']]

# 1. Move Wonder Woman to the beginning of the list
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Step 1: Move Wonder Woman to the beginning")
print(justice_league)

# 2. Separate Aquaman and Flash by inserting Green Lantern between them
aquaman_index = justice_league.index('Aquaman')
flash_index = justice_league.index('Flash')

# Remove Green Lantern and insert it between Aquaman and Flash
green_lantern = justice_league.pop(justice_league.index('Green Lantern'))
justice_league.insert(flash_index, green_lantern)
print("\nStep 2: Separate Aquaman and Flash by inserting Green Lantern")
print(justice_league)

# 3. Replace the list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nStep 3: Replace the existing list with the new members")
print(justice_league)

# 4. Sort the Justice League alphabetically and find the new leader
justice_league.sort()
new_leader = justice_league[0]
print("\nStep 4: Sorted Justice League and identified new leader")
print("Sorted Justice League:", justice_league)
print("The new leader of the Justice League is:", new_leader)
