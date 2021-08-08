# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 02:15:30 2021

@author: fatma
"""

#TAKİP KODU

import requests
from bs4 import BeautifulSoup
from send_mail import sendMail
# import time


url1 = " """urun url""" "


def checkPrice(url,paramPrice):
    headers ={
    "User-Agent":" """my user agent ile yaz""" "
}
    

    page = requests.get(url, headers=headers)

    htmlPage = BeautifulSoup(page.content,'html.parser')

    productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

    price = htmlPage.find("span",class_="prc-slg").getText()

    image = htmlPage.find("img", class_="ph-gl-img")    #get text kullanmadan fotograf olarak gonderebiliyoruz.

    convertedPrice = float(price.replace(",",".").replace(" TL",""))

    if(convertedPrice < paramPrice):
        print("Ürün fiyatı düştü")
        htmlEmailContent= """\
            <html>
            <head></head>
            <body>
            <h3>{0}</h3>
            <br/>
            {1}
            <br/>
            <p>Ürün linki: {2}</p>
            </body>
            </html>
            """.format(productTitle, image, url)
        sendMail(" """gonderen e-mail """","Ürünün fiyatı düştü👍👍", htmlEmailContent)
    else:
        print("ürün fiyatı degismedi")
    
      
    
    
checkPrice(url1, 1000)   # simdilik denerken kullandım. Dongu seklinde tekrarlanması istenirse=>
"""
#sonsuz döngüde kontrol etmesi için
while(True):
    checkPrice(url1,1000)
    time.sleep(15)       #15 saniyede bir çalışır
    
    """




# MAİL KODU 

import smtplib              #server acarken dahil ediyoruz
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject, content):     # def ile method tanımlıyoruz (bu method sadece mesaj gönderme işlevini yapar)
  
    fromMail = " """gonderen e-mail """ "   #kimden mail gidecegi
    server = smtplib.SMTP("smtp.gmail.com",587)   #host ile port belirtiyoruz

    server.starttls()     #gerekli işleme başlar, diğer katmana gönderir
    

    server.login(fromMail, " """gonderen e-mail sifresi """ ")     #eposta bilgileri girilir mail + sifre
    

    message = MIMEMultipart('alternative')     #fotografı da göstermek için 'mime' olarak belirtmek gerekir
    #içine alternative yazılır, html belgesi gndermek için gerekli
    
    message['Subject']= subject    #mesaj degiskeninde konusunu subject olarak belirtiyoruz

    htmlContent = MIMEText(content, 'html')      # icerik ve tipini(html) giriyoruz
    message.attach(htmlContent)           

    server.sendmail(     
        fromMail,
        toMail,
        message.as_string()
    )
    print("e-posta göndeildi!")
   
    server.quit()
    
