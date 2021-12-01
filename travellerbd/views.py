from django.shortcuts import render

# Create your views here.
from travellerbd.models import Destination


def index(request):
    destinations = Destination.objects.all()
    return render(request, 'index.html', {'destinations': destinations})
