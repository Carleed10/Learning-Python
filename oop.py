# class Person:
#     def __init__(self, name, age, is_male) -> None:
#         self.name = name
#         self.age = age
#         self.is_male = is_male

#     def introduce(self):
#         if not self.is_male:
#             return f"My name is {self.name}, i am {self.age} years old. I am not a male"
#         return f"My name is {self.name}, i am {self.age} years old. I am a male"
        
    
#     def walk(self):
#         return "I am walking"
    
#     def stand(self):
#         return "I am standing"


# person1 = Person("Adekunle Boluwatife", 22, True)
# person2 = Person("Igbohama Winifred", 21, False) 

# print(person1.introduce())



import math

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
      
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
       
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)

# Example execution
coordinate1 = (3, 2)
coordinate2 = (8, 10)

line_1 = Line(coordinate1, coordinate2)

print(line_1.distance())  
print(line_1.slope())  




class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):

        pi = 3.1416
        return pi * self.radius ** 2 * self.height

    def surface_area(self):

        pi = 3.1416
        return 2 * pi * self.radius ** 2 + 2 * pi * self.radius * self.height

cylinder = Cylinder(2, 3)
print(cylinder.volume())  
print(cylinder.surface_area())  
