from django.urls import path

from .views import nasabah_list, detail_nasabah

urlpatterns = [
    path('', nasabah_list),
    path('api/<int:id_nasabah>', detail_nasabah),
]