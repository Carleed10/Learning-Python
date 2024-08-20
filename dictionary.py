# phone_book = {'Bolu': "+2349087654423", 'Winnie':  "+2347088556699", 'Seun' : "+2349012366399", 'Wisdom ': "+2347088556699"}
# print(phone_book)

# print(phone_book["Bolu"])

# phone_book["John"] = "+2349088771234"
# print(phone_book)

# print("John" in phone_book)
# phone_book["Winnie"] = "+2349088771558"

my_info = {
    "name" : "Khalid",
    "age" : 22,
    "gender" : "Male"
}

print(my_info)
my_info.get("age")
print(my_info["gender"])
my_info["age"] = 30
print(my_info)

# print(my_info.get("phone_number", "Phone number doesn't exist"))