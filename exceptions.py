print("Hello World")


while True:
    try:
        age = int(input("Enter your age: "))
        result = 2024 - age
    except ValueError as e:
        print(e)
        continue
    else:
        if age < 0:
            print("Enter a valid age")
            continue
        print(result)
        break
