import string
# name = 'Khalid'
# age = 45
# height = 5.7
# is_student = False


# print("name", name)
# print("age", age)
# print("height", height)
# print("is_student", is_student)

# first_name = 'John'
# last_name = "Smith"

# print(first_name + " " + last_name)

# language = 'Python'
# print(language[0])

# greeting = 'Hello'
# print(greeting + ' Alice')

# data1 = 'Data'
# data2 = 'Science'
# print(data1 + data2)


# food = "Pizza"
# print("I love " + food)

# str_1 = "Good"
# str_2 = "Morning"
# print(str_1 + ' ' + str_2)


# text = "Concatenate"
# print(text[5])

# age =  25
# my_age  = 'I am ' + str(age) + " years old"
# print(my_age)

# city = 'New'
# space = " "
# country = "York"

# print(city + space + country)

# # alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphabets = string.ascii_uppercase
# print(alphabets[11])

# day = "Sunday"
# activity = "hiking"
# on_sunday = "On " + day + ", I am going " + activity
# print(on_sunday)



# a = "Super" 
# b = "Hero"
# print(a + b)




# # 6 & 7

# first_name = 'John'
# last_name = "Doe"
# print(first_name + last_name)


# message = 'Hello'
# print(message + ' Alice')


# # 17 - 44

# names = "James John Kennedy"
# names_list = names.split()

# print(names_list)

# cities_list = ['New York', 'Los Angeles', 'Chicago']
# cities_string = '; '.join(cities_list)

# print(cities_string)

# sentence = "the quick brown fox jumps over the lazy dog"
# print(sentence.capitalize())

# book_title =  "to kill a mockingbird"
# print(book_title.title())

# text = "hello world"
# print(text.count("o"))

# file_name = "document.txt"
# print(file_name.startswith("doc"))

# variable_url = "https://www.example.com"
# print(variable_url.endswith(".com"))


# text2 = "find the needle in the haystack"
# print(text2.find("needle"))



# name = 'Alice'
# country =  "Wonderland"

# text3 = f"Hello, {name}. Welcome to {country}."
# print(text3)


# quote = "To be or not to be"
# print(quote.find("not"))

# word = "hello"
# print(word.islower())

# word2 = "HELLO"
# print(word2.isupper())


# language = "PyThOn"
# print(language.lower())

# language = "PyThOn"
# print(language.upper())

# padded_text = " hello "
# print(padded_text.lstrip())

# padded_text = " hello "
# print(padded_text.rstrip())

# padded_text = " hello "
# print(padded_text.strip())

# greeting = "Hello World"
# print(greeting.replace("World", "Alice"))


# course_name = "Introduction to Python"
# introduction = course_name[:12]
# print(introduction)

# language = course_name[16:]
# print(language)

# quote = "To be or not to be, that is the question."
# quote_split = quote[:18]
# quote_split2 = quote[20:]
# print(quote_split2)

# phrase = "A journey of a thousand miles begins with a single step"
# print(phrase[-5:])
# print(phrase[:-7])


# str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(str[0::2])
# print(str[0:3])

# str = "tenet"
# print(str[::-1])

# learning = "Learning Python is fun and rewarding!"
# print(learning[9:19])
# print(learning[:10:2])
# print(learning[0::3])

# language = "Javascript"
# print(language[0:1])
# print(language[-1:])

# course = "DataScience"
# print(course[4:])

# greeting  = "Good Morning!"
# print(str[0::2])

# name = "Alexander"
# print(name[:3] + name[-3:])



# Monday

book_info = "harper lee ; to kill a mockingbird ; 1960 ; ISN 978-0-06-112008-4 ; 324 ; 2999.4789"
book_split = book_info.split(";")

author, title, year_published, isn, num, cost = book_split
format_author = author.title()
book_title = title.strip().title()
isbn = isn.replace("ISN", "ISBN")
cost_format = "#{0:.2f}".format(float(cost))
print(cost_format)
print(book_split)

formatted_book_info = f"The book {book_title} was written by {format_author}and published in{year_published}. It has{num}pages and{isbn} and costs {cost_format}"
print(formatted_book_info)


book_info = "george orwell ; 1984 ; 1949 ; ISN 978-0-452-28423-4 ; 328 ; 1999"
book_info_split = book_info.split(";")
author, title, year_published, isn, page, cost = book_info_split
author, title, year_published, isn, page, cost = author.strip(), title.strip(), year_published.strip(), isn.strip(), page.strip(), cost.strip()

format_author = author.title()
isbn = isn.replace("ISN", "ISBN")

# cost_format = "#{0:.2f}".format(float(cost))
cost_format = round(float(cost), 2)

formatted_book_info = """The book {} was written by {} and published {}. 
It has {} pages and {} and costs {}""".format(title, format_author, year_published, page,isbn, cost_format)
print(formatted_book_info)



