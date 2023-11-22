import imaplib
import email

def process_email():
    # 连接到IMAP服务器
    mail = imaplib.IMAP4_SSL('imap.example.com')
    
    # 登录邮箱
    mail.login('your_email@example.com', 'password')
    
    # 选择邮箱文件夹
    mail.select('inbox')
    
    # 搜索符合条件的邮件
    result, data = mail.search(None, 'ALL')
    
    # 获取邮件ID列表
    email_ids = data[0].split()
    
    # 遍历邮件ID列表
    for email_id in email_ids:
        # 获取邮件
        result, data = mail.fetch(email_id, '(RFC822)')
        raw_email = data[0][1]
        
        # 解析邮件
        msg = email.message_from_bytes(raw_email)
        
        # 提取邮件信息
        subject = msg['Subject']
        sender = msg['From']
        body = ''
        
        if msg.is_multipart():
            for part in msg.get_payload():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8')
        else:
            body = msg.get_payload(decode=True).decode('utf-8')
        
        # 处理邮件
        # TODO: 在这里编写自己的处理逻辑
        
        # 打印邮件信息
        print('Subject:', subject)
        print('Sender:', sender)
        print('Body:', body)
        print('-----------------------------------')
    
    # 关闭连接
    mail.close()
    mail.logout()
    
# 执行自动处理邮件
process_email()
