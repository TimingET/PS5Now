import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup


# setSubject convert the html file into a soup Obj to find the title tag.
# After that soup tries to find title and trim the whole tag.
# It returns the trimmed tag as String


def sendMail(htmlfile, sender, receiver, mailhost, mailhostport, password):
    global send
    # Get Config Sender and Receiver Address from ConfigDataMailinput and set it in me and you
    me = sender
    you = receiver

    htmlset = htmlfile.read()

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    # Set the trimmed title from htmlfile as Subject
    msg['Subject'] = "Playstation ist da!!"
    # Sender
    msg['From'] = me
    # Receiver
    msg['To'] = you

    # Set the Mime part
    part1 = MIMEText(htmlset, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)

    # Send the message via local SMTP server.

    mail = smtplib.SMTP(mailhost, mailhostport)

    mail.ehlo()

    mail.starttls()
    # Try to send the complete Mail
    try:
        mail.login(sender, password)
        mail.sendmail(me, you, msg.as_string())
        print('Send Mail!')
        mail.quit()
    except:
        print('Error! Mail could not send')
