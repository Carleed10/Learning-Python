# instruments = {"drums", "keyboard", "recorder", "flute"}
# print(instruments)

# my_set = {0, False}
# my_set = {0, False, 1, True}
# print(type(instruments))
# instruments = set(instruments)
# print(type(instruments))

# numbers = {0, 1, 8, 9, 2, 3, 1, 0}
# for num in numbers:
#     if num == 9:
#         print("9 is in the set")

# instruments = {"drums", "keyboard", "recorder", "flute"}
# other_instruments = {"saxophone", "trumpet", "violin"}

# print(instruments)
# instruments.add("piano")
# print(instruments)

# print(other_instruments)
# other_instruments.remove("trumpett")
# print(other_instruments)
# print(instruments)
# instruments.clear()
# print(instruments)

# del instruments

# print(instruments)


cars = {"Lexus", "Toyota", "Ferrari", "Honda", "Rolls Royce", "Tesla"}
other_cars = {"Chevrolet", "Volkswagen", "Volvo", "Audi", "Acura", "Pagani", "Lexus"}
even_more_cars = {"Innoson", "Hellcat", "Jaguar", "Xiaomi", "Lamborghini", "Audi"}

# cars = cars.intersection(other_cars).intersection(even_more_cars)
# other_cars.intersection_update(even_more_cars)

intersection = cars ^ other_cars ^ even_more_cars

# difference = cars.difference(other_cars)
cars.symmetric_difference_update(other_cars)
print(cars)

# cars.update(other_cars)
# print(intersection)
