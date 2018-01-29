from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Line
from .dict import *


# Create your views here.
def group_list(request):
    list_of_groups = list(Line.objects.all().values_list('name', flat=True))
    return JsonResponse({'groups': list_of_groups})


def alaki(request):
    print('hello')
    return HttpResponse("hello")
