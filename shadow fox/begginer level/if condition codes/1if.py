height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))       
#  Calculating BMI using the formula                           
bmi = weight / (height ** 2)
#  Determining the BMI category			
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")
