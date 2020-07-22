import os

this_file_path = os.path.abspath(__file__)
# print(this_file_path)
BASE_DIR = os.path.dirname(this_file_path)
# print(BASE_DIR)
# email_text = 'templates\email.txt'
email_text = os.path.join(BASE_DIR, 'templates', 'email.txt')

with open(email_text, 'r') as f:
    content = f.read()

# print(globals())
# print(locals())
print(content.format(name='Ajay'))
