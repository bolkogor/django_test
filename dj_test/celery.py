import os

from celery import Celery
# from parcel.models import Parcel

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_test.settings')

app = Celery('dj_test')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'parcel.tasks.calculate_delivery_cost',
        'schedule': 5.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'

