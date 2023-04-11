import imaplib

# E-posta hesap bilgileri
username = 'Password'
password = 'Şifre'

# Bağlantı kurulacak sunucu ve port numarası
imap_url = 'outlook.office365.com' # gmail için imap_url = 'imap.gmail.com'
port = 993

# Bağlantı kurulumu
mail = imaplib.IMAP4_SSL(imap_url,port)
mail.login(username,password)

# Gelen kutusu seçimi
mail.select('inbox')

# E-posta adreslerinin okunması
with open('saved_mails.txt', 'r') as f:
    email_addresses = f.readlines()
email_addresses = [email_address.strip() for email_address in email_addresses]

# E-postaların silinmesi
for email_address in email_addresses:
    _, search_data = mail.search(None,f'(FROM "{email_address}")')
    for num in search_data[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')

# Değişikliklerin kaydedilmesi ve bağlantının sonlandırılması
mail.expunge()
mail.close()
mail.logout()