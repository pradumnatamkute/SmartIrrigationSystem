 #Email your friend using python

import smtplib

receiver=input('enter the receiver email ID :')
msg=input('enter the message :')

s=smtplib.SMTP('smtp.gmail.com',587)  # s is object which connect to gmail server 

s.ehlo()
s.starttls()

s.login('from@email.com','passwd')

s.sendmail('to@email.com',receiver,msg)

s.close()

