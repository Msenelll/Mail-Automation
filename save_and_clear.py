import imaplib

# E-posta hesap bilgileri
username = 'mail adresi'
password = 'şifre'

# Bağlantı kurulacak sunucu ve port numarası
imap_url = 'outlook.office365.com' # gmail için imap_url = 'imap.gmail.com'
port = 993


# Bağlantı kurulumu
mail = imaplib.IMAP4_SSL(imap_url,port)
mail.login(username,password)

# Gelen kutusu seçimi
mail.select('inbox')

# E-posta adreslerinin okunması
with open('email_addresses.txt', 'r') as f:
    email_addresses = f.readlines()
email_addresses = [email_address.strip() for email_address in email_addresses]

# E-postaların silinmesi
_, search_data = mail.search(None,'ALL')
for num in search_data[0].split():
    _, data = mail.fetch(num,'BODY[HEADER.FIELDS (FROM)]')
    sender = data[0][1].decode('utf-8').split(':')[1].strip()
    if sender not in email_addresses:
        mail.store(num, '+FLAGS', '\\Deleted')

# Değişikliklerin kaydedilmesi ve bağlantının sonlandırılması
mail.expunge()
mail.close()
mail.logout()