from django.http import JsonResponse
from django.shortcuts import render

from .models import Line


# Create your views here.
def group_list(request):
    list_of_groups = list(Line.objects.all().values_list('name', flat=True))
    return JsonResponse({'groups': list_of_groups})
