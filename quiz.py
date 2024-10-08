school = {
    "class1": {
        "students": ["Alice", "Bob"],
        "teacher": "Mr. Smith"
    },
    "class2": {
        "students": ["Charlie", "David"],
        "teacher": "Ms. Johnson"
    }
}
print(school["class2"]["teacher"])


company = {
    "HR": ["Alice", "Bob"],
    "Engineering": ["Charlie", "David"]
}
print(company["Engineering"][1])

university = {
    "faculty": {
        "professors": ["Dr. Smith", "Dr. Brown"],
        "assistants": ["Ms. Green", "Mr. White"]
    },
    "students": ["John", "Jane", "Alice", "Bob"]
}
print(university["faculty"]["assistants"][1])

store = {
    "fruits": [
        {"name": "apple", "price": 0.5},
        {"name": "banana", "price": 0.2},
        {"name": "cherry", "price": 1.5}
    ],
    "vegetables": [
        {"name": "carrot", "price": 0.3},
        {"name": "lettuce", "price": 1.0},
        {"name": "onion", "price": 0.4}
    ]
}
print(store["fruits"][2]["price"])


library = {
    "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
    "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
}
print(library["non-fiction"][1])

family = {
    "parents": ["John", "Jane"],
    "children": [
        {"name": "Tom", "age": 5},
        {"name": "Lucy", "age": 8}
    ]
}
print(family["children"][0]["age"])

restaurant = {
    "menu": {
        "appetizers": ["soup", "salad"],
        "main_courses": ["steak", "pasta"],
        "desserts": ["cake", "ice cream"]
    },
    "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
}
print(restaurant["menu"]["main_courses"][1])


workspace = {
    "desks": [
        {"user": "Alice", "department": "HR"},
        {"user": "Bob", "department": "Engineering"}
    ],
    "equipment": {"computers": 20, "printers": 10}
}
print(workspace["desks"][0]["department"])

team = {
    "developers": ["Dev A", "Dev B"],
    "designers": ["Designer X", "Designer Y"],
    "projects": ["Project 1", "Project 2"]
}
print(team["designers"][1])

travel = {
    "domestic": ["Boston", "Chicago"], 
    "international": ["Paris", "Tokyo"],
    "expenses": {"flights": 1500, "hotels": 2000}
}

print(travel["international"][1])



