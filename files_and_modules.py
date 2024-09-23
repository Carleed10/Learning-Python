# with open("my_file.html", "a") as f:
#     f.write("<h1>I added this line using python.</h1> \n")



# with open("oop.py", "r") as f:
#     contents = f.read()

# print(contents)

# with open("oop.py", "r") as f:
#     contents = f.readlines()

# for line in contents:
#     print(line)



with open("conditional.py", "r") as f:
    contents = f.readlines()

for i, line in enumerate(contents):
    print(f"Line {i + 1}, {line}")