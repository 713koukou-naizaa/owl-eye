import smtplib
from email.message import EmailMessage
from owl_eye.config.config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_RECIPIENT, EMAIL_SENDER

def send_email(subject, body, attachments=[]):
    msg = EmailMessage()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT
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
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            return True
    except Exception:
        return False
