import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()

smtp_object.starttls()

#password = input('What is your password: ')
#password = getpass.getpass('What is your password: ')

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email, password)

from_adress = email
to_adress = 'johnmorgan258@gmail.com'
subject = input("enter the subject line: ")
message = input("enter the body message: ")
msg = "Subject: "+subject+'\n'+message


smtp_object.sendmail(from_adress, to_adress, msg)
smtp_object.quit()