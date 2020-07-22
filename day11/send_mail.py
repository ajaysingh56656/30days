import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from day11.templates import Template

username = 'dangerdevloper@gmail.com'
password = 'ajayankur2025'


class Emailer:
    from_email = 'AJAY <dangerdevloper@gmail.com>'
    has_html = False
    test_send = False

    def __init__(self, subject='', template_name=None, context=None, template_html=None, to_email=None,
                 test_send=False):
        # if not template_name and not template_html:
        if template_name is None and template_html is None:
            raise Exception('You must set a template')
        assert isinstance(to_email, list)
        if template_html:
            self.has_html = True
        self.template_html = template_html
        if not context:
            context = {}
        self.context = context
        self.to_email = to_email
        self.subject = subject
        self.template_name = template_name
        self.test_send = test_send

    def format_msg(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ', '.join(self.to_email)
        msg['Subject'] = self.subject

        if self.template_name:
            tmpl_str = Template(template_name=self.template_name, context=self.context)
            txt_part = MIMEText(tmpl_str.render(), 'plain')
            msg.attach(txt_part)
        if self.template_html:
            tmpl_str = Template(template_name=self.template_html, context=self.context)
            html_part = MIMEText(tmpl_str.render(), 'html')
            msg.attach(html_part)
        msg_str = msg.as_string()
        return msg_str

    def send_mail(self):
        msg = self.format_msg()
        # login to my smtp server
        if not self.test_send:
            with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
                server.ehlo()
                server.starttls()
                server.login(username, password)
                try:
                    server.sendmail(self.from_email, self.to_email, msg)
                    did_send = True
                except:
                    did_send = False
            return did_send


if __name__ == '__main__':
    mail = Emailer(subject='Hello World', template_name='hello.html', to_email=['ajaysingh56656@gmail.com'],
                   context={'name': 'Ajay'})
    check = mail.send_mail()
    print(check)
