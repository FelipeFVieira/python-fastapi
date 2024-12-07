import smtplib
from app.core.config import settings
from app.utils.emails_template import Utils
class EmailService:
    @staticmethod
    def send_email(recipient_name: str, recipient_email: str, template_type: str): 

        sender_email = settings.sender_email
        sender_password = settings.sender_password  

        match (template_type):
            case "academy":
                template = Utils.template_academy(recipient_name, recipient_email)
            case "linux_creation":
                template = Utils.template_linux_creation(recipient_name, recipient_email)
            case "torvalds_biography":
                template = Utils.template_torvalds_biography(recipient_name, recipient_email)
            case _:
                raise ValueError(f"Unknown template: {template_type}")
        try:
            # Configura e envia o e-mail
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(template)
                print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")