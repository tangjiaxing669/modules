# modules

### send_mail.py

```python
if __name__ == '__main__':
    HOST = 'smtp.gmail.com'
    SUBJECT = 'test email from python'
    TO = ('***@qq.com', '***@gmail.com', '***@qq.com')
    FROM = '***@gmail.com'
    CONTENT = ''' Ppython send information.
              access_num 123
              page_um 1231231
              click_num 1231231
              data 23M
              num 3
              '''
    test = SendMail(HOST, 587, FROM, TO, SUBJECT)
    test.login_mail(FROM, 'YourPassword')
    test.send_text(CONTENT)
    test.send()
```
