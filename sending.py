import settings as s

#EMAIL
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_massage(mail_content, subject):
    sender_address = s.sender_address
    sender_pass = s.sender_psw
    receiver_address = s.receiver_address
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject 
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.office365.com', 587) 
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    return True


# TELEGRAMM
import asyncio
from telegram import Bot

def sent_message_bot(text):
    async def send_message_async(text):
        bot = Bot(token=s.token)
        user_chat_id = s.user_chat_id
        message_text = text
        await bot.send_message(chat_id=user_chat_id, text=message_text)

    # Запускаем асинхронный цикл
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_async(text))
    return "Отправлено!"

