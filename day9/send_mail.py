import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'dangerdevloper@gmail.com'
password = 'ajayankur2025'


def send_mail(text='Email Body', subject='Hello World',
              from_email='AJAY <dangerdevloper@gmail.com>', to_email=None, html=None):
    assert isinstance(to_email, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html:
        html_part = MIMEText('<h1> Hi, This is none</h1>', 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg_str)
    server.quit()


if __name__ == '__main__':
    send_mail(to_email=['ajaysingh56656@gmail.com'])
    print('check it')
