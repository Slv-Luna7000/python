# Create a program that calculates your Bmi
Weight=float(input("Enter your weight :"))
Height=float(input("Enter your height :"))

bmi=Weight/(Height**2)
if bmi < 18.5:
  print(f"{bmi} Underweight")
elif 18.5 <= bmi <= 24.9:
  print(f"{bmi} Normal Weight")
elif 25<= bmi <= 29.9:
  print(f"{bmi} Overweight")
else:
  print(f"{bmi} Obese")

