import re

with open('emails.txt', 'r') as f:
    text = f.read()

emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

print(len(emails))
with open('pure_emails.txt', 'a') as f:
    for email in emails:
        f.write(email + '\n')