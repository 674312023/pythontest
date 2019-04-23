#coding utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# ----------1.跟发件相关的参数
smtpserver = "smtp.163.com" # 发件服务器
port = 0 # 端口
sender = "18159430635@163.com" # 账号
psw = "20110678lsh" # 密码
# receiver = ["xxxx@qq.com"] # 单个接收人也可以是 list
receiver = ["674312023@qq.com", '851133988@qq.com'] # 多个收件人 list 对象
# ----------2.编辑邮件的内容------
# 读文件
file_path = "result.html"
with open(file_path,'rb') as f:
    mail_body = f.read()

msg = MIMEMultipart()
msg['from'] = sender
msg['to'] = ";".join(receiver)
msg['subject'] = '测试主题'
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
#附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)

# ----------3.发送邮件------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver) # 连服务器
    smtp.login(sender, psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw) # 登录
smtp.sendmail(sender, receiver, msg.as_string()) # 发送
smtp.quit() # 关闭


