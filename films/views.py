from django.shortcuts import render
from .models import Film

def index(request):
    film_list = Film.objects.all()

    context = {
        "film_list": film_list,
    }
    return render(request, "films/index.html", context)
