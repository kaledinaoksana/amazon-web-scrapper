import settings as s

#EMAIL
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication

def send_massage(body, subject, attachment_path):
    sender_address = s.sender_address
    sender_pass = s.sender_psw
    receiver_address = s.receiver_address
    
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject 
    message.attach(MIMEText(body, 'plain'))
    
    # Attach the file
    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=attachment_path.split("/")[-1])
        part['Content-Disposition'] = f'attachment; filename="{attachment_path.split("/")[-1]}"'
        message.attach(part)
    
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
from telegram import Bot, InputFile
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

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

async def sent_message_bot_with_file(text, file):
    bot = Bot(token=s.token)
    chat_id = s.user_chat_id 
    file_path = file 

    with open(file_path, 'rb') as f:
        file = InputFile(f)

    await bot.send_document(chat_id=chat_id, document=file, caption=text)

