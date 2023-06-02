from django.urls import path, include
from eseme_app.views import zones_list

urlpatterns = [
    path('zones/', zones_list, name='zones')
]
