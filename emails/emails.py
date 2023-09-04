import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


class Emails:

    def __init__(self, from_email, to_emails, subject, html_content):
        self.from_email = from_email
        self.to_emails = to_emails
        self.subject = subject
        self.html_content = html_content

    def send_emails(self):
        message = Mail(
            from_email=self.from_email,
            to_emails=self.to_emails,
            subject=self.from_email,
            html_content=self.html_content
        )
        try:
            sg = SendGridAPIClient(settings.SG_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

