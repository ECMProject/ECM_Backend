from django.shortcuts import render
from eseme_app.models import Zones, Schedule
from django.http import JsonResponse
    
def zones_list(request):
    form = Zones.objects.all()
    context = {'form': form}
    return render(request, 'templates/index.html', context)
