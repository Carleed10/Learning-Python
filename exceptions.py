print("Hello World")

# while True:
#     try:
#         age = int(input("Enter your age: "))
#         result = 2024 - age
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         if age < 0:
#             print("Enter a valid age")
#             continue
#         print(result)
#         break



# class NegativeNumberError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError(f"The number {number} is negative.")
#     else:
#         print(f"The number {number} is positive.")


# try:
#     check_positive(int(input('Enter any number : ')))
# except NegativeNumberError as e:
#     print(f"Caught an exception: {e}")



def safe_divide(a, b):
    try:
        # Convert the inputs to floats
        a = float(a)
        b = float(b)

        # Perform division
        result = a / b
        return result

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except TypeError:
        return "Error: Both inputs must be numbers."

    except ValueError:
        return "Error: Inputs must be convertible to floats."


print(safe_divide(10, 2))   
print(safe_divide(10, 0))   
print(safe_divide(10, 'a')) 
print(safe_divide('x', 5))  
print(safe_divide([10], 5)) 
