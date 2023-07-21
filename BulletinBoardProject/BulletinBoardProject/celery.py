import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BulletinBoardProject.settings')
app = Celery('BulletinBoardProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
     'send_new_announcements': {
         'task': 'your_app.tasks.send_new_announcements',
         'schedule': crontab(hour=21, minute=0, day_of_week=5),
     }
}
