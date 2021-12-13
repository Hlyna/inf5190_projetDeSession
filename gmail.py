import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def envoi_email(msg,courrier):
    source_address = 'projetdesession5190@gmail.com'
    destination_address = json.dumps(courrier['courrier'])
    body = msg
    subject = "Nouvel ajout"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = source_address
    msg['To'] = destination_address
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(source_address, "supersecret")
    print("ici j'affiche courrier :")
    print(destination_address)
    text = msg
    server.sendmail(source_address, destination_address, text)
    print("email envoyé")
    server.quit()
