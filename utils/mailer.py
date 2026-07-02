import smtplib
from email.message import EmailMessage
from config.config import settings

def send_email(subject, body, attachments=[]):
    msg = EmailMessage()
    msg['From'] = settings.EMAIL_SENDER
    msg['To'] = settings.EMAIL_RECIPIENT
    msg['Subject'] = subject
    msg.set_content(body)

    for path in attachments:
        try:
            with open(path, 'rb') as f:
                file_data = f.read()
                file_name = path.split("/")[-1]
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        except Exception:
            continue

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.send_message(msg)
            return True
    except Exception:
        return False
