import smtplib
import os
from email.message import EmailMessage

def send_email(subject, content):
    """
    Sends an email with the given subject and content.
    Uses environment variables for credentials and config.
    """

    # Load credentials and config from environment variables
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    recipient = os.getenv("EMAIL_RECIPIENT", email_address)

    if not all([email_address, email_password]):
        raise ValueError("EMAIL_ADDRESS and EMAIL_PASSWORD must be set in your .env file.")

    # Type assertion - we know these are not None after the validation above
    assert email_address is not None
    assert email_password is not None

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = recipient
    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("[Email] Sent successfully.")
    except Exception as e:
        print(f"[Email] Failed to send: {e}")