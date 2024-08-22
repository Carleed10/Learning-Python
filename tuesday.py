dimensions = (10, 20, 30)
length, width, height = dimensions
print(length)  
print(width)  
print(height)  

# number 2
coordinates = (1.5, 2.5, 3.5)
x,y,z = coordinates
print(x)
print(y)
print(z)

# number 3
person = ("John", 25, "Engineer")
names,age,proffession = person
print(proffession)



# number 5
colors = ("red", "green", "blue", "yellow")
*color1,color2 = colors
print(color1)
print(color2)

# number 6
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, (age, position), departments = record
print(age) 
print(departments[0])  

# number 7
triplet = ("one", "two", "three")
var1,var2,var2 = triplet
print(var2)

# number 8
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
product_id, (category, price), (day, month, year) = info
print(category) 
print(year)  

# number 9
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
first, second, third = nested_tuple
print(third[1])  

# number 10
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
(apples, apple_qty), (bananas, banana_qty), (cherries, cherry_qty) = inventory
print(banana_qty) 
