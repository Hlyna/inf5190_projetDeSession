import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envoi_email(msg,courrier):
    source_address = 'projetdesession5190@gmail.com'
    destination_address = courrier
    body = msg
    subject = "Nouvel ajout"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = source_address
    msg['To'] = destination_address
    msg.attach(MIMEText(body, 'plain'))
    print("ici")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(source_address, "supersecret")
    print("ici j'affiche message :")
    print(msg)
    print("ici j'affiche message :")
    text = msg
    print("ici")
    print(msg)
    print("ok")
    server.sendmail(source_address, destination_address, text)
    print("email envoyé")
    server.quit()
