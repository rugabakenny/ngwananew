from django.shortcuts import render

from .models import *
from .serializers import*
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


# Create your views here.

@csrf_exempt
def home(request):
    return HttpResponse('<center><font color="steelblue"><h1>Welcome to tourism</h1></font></center>')

####..create account
@csrf_exempt
def userregisted(request):
    if request.method == 'GET':
        userreg = User.objects.all().select_related('userregisted')
        serializer = RegistedSerializer(userreg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Account created, Succcessful'}, status=201)
        return JsonResponse(serializer.errors, status=401)    

