import yagmail
import os
from dotenv import load_dotenv

load_dotenv()



sender = "annannthu@gmail.com"
receiver = "0468x9fcnw@spymail.one"
subject = 'Test main using python'
contents = '''
This is the content side for sending mail
'''

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email send!")