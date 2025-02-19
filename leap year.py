Year=int(input("Enter Year :"))

if Year %4 and Year % 100 !=0:
  print(f"{Year} is a leap year")
else:
  print(f"{Year} is not a leap year")
