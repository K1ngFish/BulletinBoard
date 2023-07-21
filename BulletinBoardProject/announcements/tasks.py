from celery import shared_task
from datetime import datetime, timedelta

from django.core.mail import EmailMessage

from .models import Announcement, User

@shared_task
def send_new_announcements():
    last_week = datetime.now() - timedelta(days=7)
    new_announcements = Announcement.objects.filter(dateCreation__gte=last_week)

    recipients = User.objects.all()

    for recipient in recipients:
        subject = "Новые объявления за неделю"
        message = "Добрый день! Вот новые объявления за последнюю неделю:\n\n"
        for announcement in new_announcements:
            message += f"- {announcement.title}\n"
        message += "\nС уважением,\nВаш сайт объявлений"

        email = EmailMessage(subject, message, "mailfortestprojects@yandex.ru", [recipient.email])
        email.send()
