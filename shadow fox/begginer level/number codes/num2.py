#2.	In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. 
# Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter
pi = 3.14
radius = 84
water_per_square_meter = 1.4                        
#  Calculating  the area of the pond        
area_of_pond = pi * radius ** 2             
#  Calculating  the total amount of water in the pond
total_water = area_of_pond * water_per_square_meter
print("The area of the pond is approximately:", round(area_of_pond, 2), "square meters.")
print("The total amount of water in the pond is:", int(total_water), "liters.")
