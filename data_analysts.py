import re
# Read the content of reviews.txt
with open("reviews.txt", "r") as f:
    content = f.read()

# Extract email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_addresses = re.findall(email_pattern, content)
print(email_addresses)

# Put email addresses in a file called emails.txt
with open("emails.txt", "w") as f:
    for email_address in email_addresses:
        f.write(f"{email_address}\n")

# Extract all phone numbers
phone_num_pattern = r"\+234 \d{3} \d{3} \d{4}"
phone_numbers = re.findall(phone_num_pattern, content)
print(phone_numbers)

# Put phone numbers in a file called phone_numbers.txt
with open("phone_numbers.txt", "w") as f:
    for phone_number in phone_numbers:
        f.write(f"{phone_number}\n")