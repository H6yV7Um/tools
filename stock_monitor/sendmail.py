#!/bin/python
# -*- coding:utf8 -*-


import smtplib
from email.mime.text import MIMEText

class Mails():
    def __init__(self, host, port,user, password):
        self.smtp = smtplib.SMTP()
        self.smtp.connect(host, port)
        self.smtp.login(user, password)

    def send(self, subject, text, mail_from, mail_to):
        msg = MIMEText(text)
        #msg = MIMEText(u"good luck")
        msg['Subject'] = subject
        msg['From'] = mail_from
        msg['To'] = mail_to[0]
        self.smtp.sendmail(mail_from, mail_to, msg.as_string())

    def __del__(self): 
        self.smtp.quit()

SINGAL_MAIL=Mails("smtp.163.com", "25", "username", "passwd!")

if __name__ == "__main__":
    a=Mails("smtp.163.com", "25", "username", "passwd")
    #a.send("subject !!!", "我们是中国人", "qxiong133@163.com", "zqx2010@gmail.com")
    a.send("subject !!!", "我们是中国人", "qxiong133@163.com", ["zqx2010@gmail.com","348297509@qq.com"])


