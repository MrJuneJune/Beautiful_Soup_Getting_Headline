# -*- coding: utf-8 -*-
"""
Created on Tue May 15 23:23:14 2018

@author: June
"""

from bs4 import BeautifulSoup
import urllib.request
import datetime
#If you want the file directly to your email
#import smtplib
#from email.message import EmailMessage
#%%
# Check the date of new with in the file.
def check():
          txt = open("Trump News.txt", 'r')
          for line in txt:
               if today in line:
                    return(True)
          return(False)
#%%
url = "websiteyouwant.com"
#req = urllib.request.urlopen(url)
# In my case, I will use koreatimes.
req = urllib.request.urlopen('http://www.koreatimes.co.kr/www2/index.asp')
# Reading it as xml file. Can be read as html as well.
xml = BeautifulSoup(req, 'xml')
# Checking Today.
today = str(datetime.date.today())
#%%
# Only getting front head line news. Class will be different for different website
# Keep in mind that this information is not yours...
for div in xml.find_all(attrs={"class":"top1_lead LD"}):
     # Finding text with in the <a> </a> in div calss front page.
     text = div.find('a').text
     # If you want to read the front page.
     href = div.find('a')['href']
     # Checking if the text has trump
     if check() == True:
          if text.find('Trump') == 0:
               txt = open("Trump News.txt", 'a')
               txt.write(today + '\n' + text)
               txt.close()
               print("You just checked today's Trump news")
               #If you want the heading to your email directly
               #msg = EmailMessage()
               # msg.set_content(text)
               #          
               #msg['Subject'] = 'Trump News'
               #msg['From'] = 'me@mail.com'
               #msg['To'] = 'me@mail.com'
               #          
               #s = smtplib.SMTP('localhost')
               #s.send_message(msg)
               #s.quit()
     else:
          print("You already checked today's news")

               
               


