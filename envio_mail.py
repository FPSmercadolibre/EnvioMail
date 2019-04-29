import smtplib, ssl
import threading

interval = 5

def send():
    #threading.Timer(interval, send).start()
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "TuEmail"#eMail
    receiver_email = input('Ingrese el mail destinatario:') 
    password = "" #Pass
    message = """\
    Subject: Este mensaje fue enviado por Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

send()
print('El mensaje fue enviado correctamente!')
