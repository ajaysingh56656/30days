import imaplib
import email

host = 'imap.gmail.com'
username = 'dangerdevloper@gmail.com'
password = 'ajayankur2025'

mail = imaplib.IMAP4_SSL(host)
login = mail.login(username, password)
# print(login)

select = mail.select('inbox')
# print(select)

_, search_data = mail.search(None, 'UNSEEN')
# print(search_data)

# for num in search_data[0]:
#     print(num)

for num in search_data[0].split():
    # print(num)
    _, data = mail.fetch(num, '(RFC822)')
    # print(data[0])
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    # print(email_message)
    for part in email_message.walk():
        if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
            body = part.get_payload(decode=True)
            print(body.decode())




