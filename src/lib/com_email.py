"""
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import email
import imaplib
import smtplib
import socket
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from lib import com_config, com_logger


def getIFFT():
    logger = com_logger.Logger('GetCommand')
    config = com_config.getConfig()
    logger.log.info('Getting command')
    command = ''
    try:
        logger.log.debug('Try to connect IMAP')
        connection = imaplib.IMAP4_SSL('imap.gmail.com')
        logger.log.debug('Connected to IMAP')
        logger.log.debug('Try to login mailbox')
        connection.login(config['EMAIL']['username'], config['EMAIL']['password'])
        logger.log.debug('Connected to mailbox')
        rv, data = connection.select('INBOX')
        if rv == 'OK':
            logger.log.debug('Check command to mailbox')
            resp, items = connection.search(None, '(UNSEEN FROM "' + config['CCM'][
                'mailfrom'] + '")')  # (FROM "Doug" SUBJECT "test message 2"
            items = items[0].split()
            for emailid in items:
                resp, data = connection.fetch(emailid, "(BODY[HEADER.FIELDS (SUBJECT)])")
                msg = email.message_from_string(str(data[0][1]))
                subject = (msg["b'Subject"].replace('\\n', '').replace('\\r', '').replace("'", ''))
                logger.log.debug(subject)
                lst = subject.split(':')
                if len(lst) == 2 and lst[0] == config['CCM']['mailsubject']:
                    logger.log.debug('Command: ' + lst[1])
                    command = lst[1]
                else:
                    logger.log.debug('Mail with no command')
            connection.close()
        connection.logout()
        logger.log.debug('Logout IMAP')
    except socket.gaierror:
        logger.log.critical('Error get command')
    finally:
        return command


def send_mail_gmail(subject, table, filename=""):
    config = com_config.getConfig()
    logger = com_logger.Logger('Email')
    logger.log.info('Sending email')
    msg = MIMEMultipart()

    body=''
    for line in table:
        body += line + "<br>"

    msg['From'] = config['EMAIL']['from']
    msg['To'] = config['EMAIL']['to']
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    try:
        if len(filename) > 0:
            attachment = open("./" + filename, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)

        logger.log.debug('Try to connect SMTP')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        logger.log.debug('Connected to SMTP')
        server.starttls()
        logger.log.debug('Try to connect mail box')
        server.login(config['EMAIL']['from'], config['EMAIL']['password'])
        text = msg.as_string()
        logger.log.debug('Connected to mailbox')
        logger.log.debug('Try to send mail')
        server.sendmail(config['EMAIL']['from'], config['EMAIL']['to'], text)
        logger.log.debug('Mail sent')
        server.quit()
    except:
        logger.log.critical('Error sending mail')


# Info Mail
# https://pymotw.com/2/imaplib/

"""
MESSAGES
The number of messages in the mailbox.
RECENT
The number of messages with the Recent flag set.
UIDNEXT
The next unique identifier value of the mailbox.
UIDVALIDITY
The unique identifier validity value of the mailbox.
UNSEEN
The number of messages which do not have the Seen flag set.
"""
