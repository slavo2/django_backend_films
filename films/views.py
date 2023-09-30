from django.shortcuts import render
from .models import Film

def index(request):
    if "filter_name" in request.GET:
        filter_by_name = request.GET["filter_name"]
        film_list = Film.objects.filter(name__contains=filter_by_name)
    else:
        filter_by_name = ""
        film_list = Film.objects.all()

    context = {
        "film_list": film_list,
        "filter_name": filter_by_name,
    }
    return render(request, "films/index.html", context)
