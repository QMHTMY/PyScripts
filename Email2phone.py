#!/usr/bin/python3
# coding:utf-8
# 发送文档到手机端

import os 
import time
import click

import smtplib 
from email import encoders 
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail():
    '''用网易邮箱发送邮件'''
    def __init__(self,to_addr,attachment=''):
        self.filename  = attachment
        self.to_addr   = to_addr
        self.from_addr = 'email address'
        self.passwd    = 'passwd'
        self.server    = 'smtp_server'

    def getTimeStr(self):
        '''获取系统时间'''
        timeStr = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()) 
        timeStr = 'xxxxxx  ' + timeStr
        return timeStr

    def message(self):
        msg = MIMEMultipart() 

        #主题和地址
        msg['To']   = self.to_addr 
        msg['From'] = self.from_addr 
        msg['Subject'] = "Your subject" 

        #正文
        body = self.getTimeStr()
        msg.attach(MIMEText(body, 'plain')) 

        #有附件时附上
        if (len(self.filename) !=0) and os.path.exists(self.filename):
            part = MIMEBase('application','octet-stream')
            with open(self.filename, 'rb') as fobj:
                part.set_payload(fobj.read()) 
                encoders.encode_base64(part) 
                part.add_header('Content-Disposition', 'attachment', filename=self.filename) 
                msg.attach(part) 

        return msg

    def send(self):
        '''设置SMTP并发送'''
        msg = self.message()
        server = smtplib.SMTP(self.server) 
        server.starttls() 
        server.login(self.from_addr , self.passwd) 
        server.sendmail(self.from_addr, self.to_addr, msg.as_string()) 
        server.quit()

helpStr = ['destination address(default is outlook.com','an attachment file(default is none)']
address= 'xxx@xx.com'
@click.command()
@click.option('--to_addr',default=address,help=helpStr[0])
@click.option('--attachment',default="",help=helpStr[1])
def sendEmail(to_addr, attachment):
    '''邮件发送'''
    sender = SendEmail(to_addr, attachment)
    sender.send()

if __name__ == "__main__":
    sendEmail()
