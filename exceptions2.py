# print("Hello world")

# name = "Bolu"

# if name == "Winnie":
#     print(12/0)
# else:
#     print("Name is not Winnie")

# try:
#     result = 12/int(input("Enter the divisor: "))
# except ZeroDivisionError as e:
#     print("cannot divide by zero")
# except ValueError as e:
#     print("The divisor must be a number")
#     print("More details: ", e)
# except Exception:
#     print("something went wrong")
# else:
#     print(result)
# finally:
#     print("This block always runs")

from datetime import datetime

class InvalidAge(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    while True:
        age = input("Enter your age: ")
        try:
            age = int(age)
        except ValueError:
            print("Age must be a number")
            continue
        else:
            try:
                if age < 0:
                    raise InvalidAge("Invalid age entered. Please try again")
            except InvalidAge as e:
                print(e)
                continue
            current_year = datetime.today().year
            birth_year = current_year - age
            print(f"You were born in {birth_year}")
            break
except KeyboardInterrupt:
    print("\nprogram terminated")




