import re


reviews_file_path = 'reviews.txt'
emails_file_path = 'emails.txt'
phone_numbers_file_path = 'phone_numbers.txt'


email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\+234\s\d{3}\s\d{3}\s\d{4}'


def extract_emails_and_phones(text):
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    return emails, phones


with open(reviews_file_path, 'r') as file:
    content = file.read()

emails, phones = extract_emails_and_phones(content)


with open(emails_file_path, 'w') as email_file:
    for email in emails:
        email_file.write(f"{email}\n")

with open(phone_numbers_file_path, 'w') as phone_file:
    for phone in phones:
        phone_file.write(f"{phone}\n")


print("Emails:", emails)
print("Phone Numbers:", phones)
