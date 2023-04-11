import re

with open('unique_emails.txt', 'r') as f:
    text = f.read()

emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

unique_emails = list(set(emails))
print(len(unique_emails))

with open('unique_emails.txt', 'w') as f:
    for email in unique_emails:
        f.write(email + '\n')