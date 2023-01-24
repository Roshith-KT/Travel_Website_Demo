from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,TeamMembers
# Create your views here.

def index(request):
    obj = Place.objects.all()
    obj2 = TeamMembers.objects.all()
    return render(request, 'index.html',{'result':obj,'result2':obj2})

