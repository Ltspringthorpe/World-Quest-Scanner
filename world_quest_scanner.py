import urllib2, re, smtplib, ssl, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def scan_active_world_quests():
    sender_email = 'myemail@gmail.com'
    receiver_email = 'myemail@gmail.com'
    password = 'mypassword'
    email_subject = ''
    email_body = ''

    strings = ['Sabertron', 'Whiplash']
    website = 'https://www.wowhead.com/world-quests/bfa/na'
    source = urllib2.urlopen(website).read()

    for string in strings:
        string = string.capitalize()
        if re.search(string, source, flags=re.IGNORECASE):
            print(string + ' found on ' + time.ctime())
            email_body += '<p>' + string + ' found on ' + time.ctime() + '!</p>'
            if len(email_subject) > 0:
                email_subject += ', ' + string
            else: email_subject = string

        else:
            print('Scan finished unsuccessfully for ' + string + ' on ' + time.ctime())

    if len(email_body) > 0:
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
