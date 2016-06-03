
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailController():

    def __init__(self):
        self.__dir_email = 'emergencypets@gmail.com'
        self.__contrasena_email = 'mayesilviaaleja'

    def enviar_email(self, para, mensaje, asunto):
        try:
            import smtplib
            msg = MIMEMultipart()
            msg['From'] = self.__dir_email
            msg['To'] = para
            msg['Subject'] = asunto
            msg.attach(MIMEText(mensaje, 'html'))
            text = msg.as_string()
            self.__server = smtplib.SMTP('smtp.gmail.com:587')
            self.__server.starttls()
            self.__server.login(self.__dir_email, self.__contrasena_email)
            self.__server.sendmail(self.__dir_email, para, text)
            self.__server.quit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False

    def enviar_email_usuario(self, de, mensaje, asunto):
        try:
            import smtplib
            msg = MIMEMultipart()
            msg['From'] = de
            msg['To'] = self.__dir_email
            msg['Subject'] = asunto
            msg.attach(MIMEText(mensaje, 'html'))
            text = msg.as_string()
            self.__server = smtplib.SMTP('smtp.gmail.com:587')
            self.__server.starttls()
            self.__server.login(self.__dir_email, self.__contrasena_email)
            self.__server.sendmail(de, self.__dir_email, text)
            self.__server.quit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False