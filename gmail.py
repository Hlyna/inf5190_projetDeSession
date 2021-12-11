import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

source_address = 'projetdesession5190@gmail.com'
destination_address = "hamza.lyna@courrier.uqam.ca"
body = "Bonsoir Maya, je vous annonce que vous êtes officiellement residente du canada."
subject = "VERY IMPORTANT !"

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = source_address
msg['To'] = destination_address
msg['ReplyTo'] = "justintrudeau@uqam.ca"

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(source_address, "supersecret")
text = msg.as_string()
server.sendmail(source_address, destination_address, text)
server.quit()
