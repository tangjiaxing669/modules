#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "Jason Tom"

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

'''
Note: If you can't send the mail, plese go to this link and select Turn on.
https://www.google.com/settings/security/lesssecureapps
'''

def mail_judge(mail_addr):
    '''
    Note: To judge mail address is legitimate.
    :param mail_addr: It's mail address
    :return: bool type
    '''
    return str(mail_addr[1:]).find('@') != -1 and str(mail_addr).endswith(('.com', '.cn', '.net', '.org', 'gov'))

class SendMail:
    def __init__(self, smtp_host, smtp_port, mail_from, mail_to, mail_subject):
        '''
        Note: initial variable and judge
        :param smtp_host: SMTP host. < smtp.gmail.com >
        :param smtp_port: SMTP port. < 587 >
        :param mail_from: mail sender. < *****@gmail.com >
        :param mail_to: mail recipient, It's list type. < ['***@gmail.com', '***@gmail.com', ...] >
        :param mail_subject: mail subject.
        '''
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.mail_from = mail_from
        self.mail_to = mail_to
        self.mail_subject = mail_subject

        if not isinstance(self.mail_to, tuple):
            raise Exception('The {!r} should by a tuple type.'.format(self.mail_to))

        for i in self.mail_to:
            if not mail_judge(i):
                raise Exception('The {!r} error for mail address format.'.format(i))

        if not mail_judge(self.mail_from):
            raise Exception('The {!r} error for mail address format.'.format(self.mail_from))

    def __del__(self):
        pass

    def login_mail(self, login_user, login_pass, debug=False, smtp_timeout=5):
        '''
        Note: Create SMTP object and login to self.smtp_host.
        :param login_user: Login to SMTP server for username.
        :param login_pass: Login to SMTP server for password.
        :param debug: Judge DEBUG info turn off/on.
        :param smtp_timeout: SMTP server connection timeout, default 5s.
        :return: None
        '''
        try:
            self.sm = smtplib.SMTP(host=self.smtp_host, port=self.smtp_port, timeout=smtp_timeout)
            if debug:
                self.sm.set_debuglevel(1)
            self.sm.ehlo()
            self.sm.starttls()
            self.sm.ehlo()
            self.sm.login(login_user, login_pass)
        except Exception as e:
            print("Failed: {0}".format(e))
            sys.exit()

    def send_text(self, mail_content):
        '''
        Note: Define mail content.
        :param mail_content: mail content.
        :param img: send to img for email.
        :return: None
        '''
        self._body = '\r\n'.join(['From: %s' % self.mail_from,
                                 'To: %s' % ','.join(self.mail_to),
                                 'Subject: %s' % self.mail_subject,
                                 ' ',
                                 '%s' % mail_content])

    def send_html(self, html_content):
        '''
        Note: Define mail content for html format.
        :param html_content: HTML format for mail content
        :return: None
        '''
        html_content = str(html_content).encode('utf-8')
        self._msg = MIMEText(html_content, "html", "utf-8")
        self._msg['Subject'] = self.mail_subject
        self._msg['From'] = self.mail_from
        self._msg['To'] = ','.join(self.mail_to)
        self._body = self._msg.as_string()

    def send(self):
        '''
        Note: Just send mail.
        :return: None
        '''
        try:
            for i in range(len(self.mail_to)):
                self.sm.sendmail(self.mail_from, self.mail_to[i], self._body)
                print('Send mail from {0} to {1} Success. '.format(self.mail_from, self.mail_to[i]))
                # yield True
        except Exception as e:
            print('Send Failed: {0}'.format(e))
            sys.exit()
