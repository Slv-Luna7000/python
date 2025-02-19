# List data structures
fruits=["Mangoes","Apple","Kiwi","Grapes","Oranges","Banana"]
print(fruits)
print(f"I love eating {fruits[1]}")
numbers=[1,3,5,8,1,4,0,-2,5]
numbers.sort()
numbers.append("Pineapples")
numbers.pop(1)
numbers.reverse()
print(numbers[6])
print(numbers)

# tuple data structures
# its ordered
# has index
cars=("Mercedes","toyota","Honda","Subaru","Rover","Mazda","Nissan","Vw")
numbari=(3,9,8,1,0,4,5,33,8,-65)
print(cars)
print(f"Japan produces{cars[2]}")
print(numbari)
print(sorted(numbari))

# set data structures
# not ordered
# not index
country={"Kenya","Uganda","Tanzania","Burundi","Rwanda","Usa","Dubai","Mexico"}
print(country)
country.pop()
print(country)

# Dictionary data structure
students={"Name":"Aisha","Age":"18","Gender":"Female","Phone number":712317428}
students['Name']="Ilhan"
print(f"My name is {students['Name']} and im {students['Age']} years old. My gender is {students['Gender']} and my phone number is {students['Phone number']}")
