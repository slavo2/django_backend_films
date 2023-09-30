from django.http import HttpResponse
from django.template import loader
from .models import Film

def index(request):
    film_list = Film.objects.all()

    template = loader.get_template("films/index.html")
    context = {
        "film_list": film_list,
    }
    return HttpResponse(template.render(context, request))
