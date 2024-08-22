fruits = {"air", "water", "food"}
print("food" in fruits)

colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)


animals = {"cat", "dog", "rabbit"} 
multiple_items = ["horse", "sheep"]
animals.update(multiple_items)
print(animals)


countries = {"USA", "Canada", "Mexico"}
countries.remove("Canada")
print(countries)

# cities = {"New York", "Los Angeles", "Chicago"}
# cities.remove("Houston")


seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
unique_seasons = set(seasons)
print(unique_seasons)

set1 = {1, 2, 3} 
set2 = {3, 4, 5}
union = set1.union(set2)
print(union)

setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
intersection = setA.intersection(setB)
print(intersection)


prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(prime_numbers)


odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.pop()
print(odd_numbers)


vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)


letters = {"a", "b", "c"}
another_letter = {"b", "c", "d"}
diff = letters.symmetric_difference(another_letter)
print(diff)



tech_brands ={"Apple", "Google", "Microsoft"}
new_set = {"Amazon", "Facebook"}
tech_brands.update(new_set)
print(tech_brands)


students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Alice")
# students.remove("Eve")
print(students)

numbers_list = [1, 2, 3, 4, 4, 5, 5]
numbers_set = set(numbers_list)
print(numbers_set)

text = "hello"
unique_characters = set(text)
print("Unique characters in 'hello':", unique_characters)

vehicles = {"car", "bike", "bus", "train"}
print(len(vehicles))


gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
num_gadgets = len(gadgets)
print(num_gadgets)
