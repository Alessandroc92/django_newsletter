from django.core.mail import send_mass_mail
from django.tasks import task

from . import services


@task()
def send_happy_bday_emails(**kwargs):
    emails = services.create_emails_from_templates(**kwargs)
    send_mass_mail(emails, fail_silently=False)
