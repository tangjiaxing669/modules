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



#if __name__ == '__main__':
#    HOST = 'smtp.gmail.com'
#    SUBJECT = 'Test email from Python'
#    TO = ('1551694017@qq.com', '330547236@qq.com')
#    FROM = 'jasontom147@gmail.com'
#    CONTENT = '''<table width="800" border="0" cellspacing="0" cellpadding="4">
#    <tr>
#        <td bgcolor="#CECFAD" height="20" style="font-size:14px">* 官网数据 <a href="monitor.domain.com">更多</a></td>
#    </tr>
#    <tr>
#        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
#            1) 日访问量: <font color=red>152433</font> 访问次数: 23651 页面浏览量: 45123 点击数: 545122 数据流量: 504Mb<br>
#            2) 状态码信息<br>
#            &nbsp;&nbsp;500:105  404:3264  503:214<br>
#            3) 访客浏览器信息<br>
#            &nbsp;&nbsp;IE:50%  firefox:10%  chrome:30%  other:10%<br>
#            4) 页面信息<br>
#            &nbsp;&nbsp;/index.php 42153<br>
#            &nbsp;&nbsp;/view.php 21451<br>
#            &nbsp;&nbsp;/login.php 51112<br>
#        </td>
#    </tr>
#</table>'''
#    CONTENT_1 = '''Python send information.
#                access_num 23651
#                page_num 45123
#                click_num 545122
#                data 504Mb
#                num  3'''
#    test = SendMail(HOST, 587, FROM, TO, SUBJECT)
#    test.login_mail(FROM, 'tjb6045011')
#    test.send_text(CONTENT_1)
#    test.send()