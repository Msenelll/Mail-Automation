import email
import imaplib

# E-posta hesap bilgileri
username = 'email adresi'
password = 'şifre'

# Bağlantı kurulacak sunucu ve port numarası
imap_url = 'imap.gmail.com' # gmail için imap_url = 'imap.gmail.com' # outlook için imap_url = 'outlook.office365.com'
port = 993 

# Bağlantı kurulumu
mail = imaplib.IMAP4_SSL(imap_url,port)
mail.login(username,password)

# Gelen kutusu seçimi
#gmail için mail.select('inbox') # Gelen kutusu için 'inbox' yazılır. Diğer klasörler için 'INBOX/klasör adı' yazılır.
mail.select('inbox') # Gelen kutusu için 'inbox' yazılır. Diğer klasörler için 'INBOX/klasör adı' yazılır.

# Tüm e-postaların aranması
_, search_data = mail.search(None,'ALL')

# E-posta gönderen adreslerinin alınması
email_list = []
for num in search_data[0].split():
    _, data = mail.fetch(num,'(RFC822)') # RFC822: E-posta içeriğinin tamamını almak için kullanılır.
    _, b = data[0] # b: E-posta içeriğini byte tipinde tutar.
    email_message = email.message_from_bytes(b) # E-posta içeriğini okunabilir hale getirir.
    email_from = email_message['From'] # E-posta gönderen adresini alır.
    if email_from not in email_list:
        email_list.append(email_from)
        print(email_from)

with open('emails.txt','w') as file:
    for email_address in email_list:
        
        file.write(email_address + '\n')
# Bağlantının sonlandırılması
mail.close()
mail.logout()