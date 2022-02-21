import urllib2, re, smtplib, ssl, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def scan_active_world_quests(email = False):

    if email == True:
        sender_email = 'myemail@gmail.com'
        receiver_email = 'myemail@gmail.com'
        password = 'mypassword'
        email_subject = ''
        email_body = ''

    key_words = [
        'Oozing with Character',
        'Deadly Reminder'
    ]
    website = 'https://www.wowhead.com/world-quests/sl/na'
    source = urllib2.urlopen(website).read()
    print(time.ctime() + ' - Scanning...')

    for key_word in key_words:
        key_word = key_word.title()
        if re.search(key_word, source, flags=re.IGNORECASE):
            print(u'\u2713 ' + key_word)

            if email == True:
                email_body += '<p>' + key_word + ' found on ' + time.ctime() + '!</p>'
                if len(email_subject) > 0:
                    email_subject += ', ' + key_word
                else: email_subject = key_word

        else:
            print('  ' + key_word)

    if email == True and len(email_body) > 0:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = email_subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        body = '<html><body>' + email_body + '</body></html>'
        html = MIMEText(body, 'html')

        msg.attach(html)
        s = smtplib.SMTP_SSL('smtp.gmail.com')
        s.login(sender_email, password)

        s.sendmail(sender_email, receiver_email, msg.as_string())
        s.quit()

while True:
    interval = 21600 # in seconds, 21600 seconds = 6 hours
    scan_active_world_quests()
    time.sleep(interval)
