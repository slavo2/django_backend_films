import requests
from .models import Film
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

def update_db():
    r = requests.get(settings.URL_FOR_UPDATING_FILM_DATABASE)
    remote_data = r.json()
    if remote_data:
        Film.objects.all().delete()
        for film_data in remote_data:
            film = Film(data=film_data)
            film.load_data()
            film.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_db, 'interval', minutes=settings.FILM_DATABASE_UPDATE_INTERVAL)
    scheduler.start()