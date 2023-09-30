from django.shortcuts import render
from .models import Film

def index(request):
    if "filter_by_name" in request.GET:
        filter_by_name = request.GET["filter_by_name"]
        film_list = Film.objects.filter(name__contains=filter_by_name)
    else:
        filter_by_name = ""
        film_list = Film.objects.all()
    
    if "order_by_name" in request.GET:
        order_by_name = request.GET["order_by_name"]
        if order_by_name == "DESC":
            film_list = film_list.order_by("-name")
        elif order_by_name == "ASC":
            film_list = film_list.order_by("name")
        else:
            order_by_name = ""
    else:
        order_by_name = ""

    context = {
        "film_list": film_list,
        "filter_by_name": filter_by_name,
        "order_by_name": order_by_name,
    }
    return render(request, "films/index.html", context)
