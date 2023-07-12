# IMPORT LIB

from bs4 import BeautifulSoup
import pandas as pd
import requests

import time
import datetime
import smtplib #for sending emails
import csv
import datetime
import os
import csv
import smtplib
import settings as s
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# CONNECTION
def connect(URL):
    headers = s.headers
    page = requests.get(URL,headers=headers)
    bs = BeautifulSoup(page.content, "html.parser")
    return BeautifulSoup(bs.prettify(), 'html.parser')

# OPEN TITLE
def find_title(bs):
    title = bs.find(id="productTitle").get_text().strip()
    return title

# PRICE : FIND FIRST SPAN WHERE class = "a-offscreen"
def find_price(bs):
    price = bs.find("span", {"class": "a-offscreen"}).get_text().strip().replace('$','')
    return price

# SAVE DATA TO FILE
def write_data(file, title, price):

    today = datetime.date.today()
    header = ['Title','Price','Date']
    data = [title, price, today]
    type(data)
    if os.path.isfile(file):
        with open(file,'a+', newline = '', encoding = 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    else:
        with open(file,'w', newline = '', encoding = 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)
    return True


#CHECK PRICE
def check_price(price, min_price):
    if (float(price) < float(min_price)):
        send_massage()
        return True
    return False

# SEND MESSAGE
def send_massage():
    mail_content = "hh"
    sender_address = s.sender_address
    sender_pass = s.sender_psw
    receiver_address = s.receiver_address
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.office365.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    return True


# MAIN
file = 'files/AmazonWebScraper.csv'
URL = 'https://www.amazon.com/Amazon-Essentials-Womens-Skirt-Camel/dp/B08JH893DJ/ref=sr_1_2?crid=2EPWJXDHO814T&keywords=skirt&qid=1686339482&sprefix=skirt%2Caps%2C213&sr=8-2&th=1&psc=1'
low_price = 25

bs = connect(URL)
price = find_price(bs)
title = find_title(bs)

if write_data(file, title, price):
    pd.read_csv(file)

if check_price(price, low_price):
    print('price of',title,'lower than', low_price, 'AND =', price)
else:
    print('price of',title,'higher than', low_price, 'AND =', price)
