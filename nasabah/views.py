from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Nasabah
from .serializers import NasabahSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return HttpResponse('haloo ini adalah index nasabah!')


@csrf_exempt
def nasabah_list(request):
    if request.method == 'GET':
        nasabah = Nasabah.objects.all()
        serializer = NasabahSerializer(nasabah, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NasabahSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def detail_nasabah(request, id_nasabah):
    try:
        nasabah = Nasabah.objects.get(id_nasabah=id_nasabah)
    
    except Nasabah.DoesNotExist:
        return HttpResponse(status=404)

    if request.method== 'GET':
        serializer = NasabahSerializer(nasabah)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NasabahSerializer(nasabah, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        nasabah.delete()
        return HttpResponse(status=204)
