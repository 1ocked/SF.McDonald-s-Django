# import os
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcdonalds.settings')
#
# app = Celery('mcdonalds')
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.autodiscover_tasks()
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mcdonalds_app.settings')

app = Celery('Mcdonalds_app')

# Загрузка настроек Celery из файла settings.py Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач
app.autodiscover_tasks()