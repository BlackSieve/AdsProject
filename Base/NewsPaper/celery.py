import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Base.settings')

app = Celery('Base')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'activate_every_week_8':{
        'task':'news.tasks.weekly_send_email_task',
        'schedule': crontab(hour=8,minute=0,day_of_week='monday'),
        'args':()
    }
}