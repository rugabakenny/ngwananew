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

@csrf_exempt
def hotel(request):
   
    if request.method == 'GET':
        reg = Hotel.objects.all()
        serializer = HotelSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = HotelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)  
@csrf_exempt
def travel(request):
   
    if request.method == 'GET':
        reg = Travel.objects.all()
        serializer = TravelSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = TravelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400) 

def currency(request):
   
    if request.method == 'GET':
        reg = travel.objects.all()
        serializer = CurrencySerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = CurrencySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400) 

def mokoro(request):
   
    if request.method == 'GET':
        reg = Mokoro.objects.all()
        serializer = MokoroSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = MokoroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400) 



        
def boat(request):
   
    if request.method == 'GET':
        reg = Boat.objects.all()
        serializer = BoatSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = BoatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400) 

       
def nightclub(request):
   
    if request.method == 'GET':
        reg =Nightclub.objects.all()
        serializer = NightclubSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = NightclubSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400) 
    
def carrental(request):
   
    if request.method == 'GET':
        reg =Carrental.objects.all()
        serializer =CarrentalSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = CarrentalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400) 

    
def restaurant(request):
   
    if request.method == 'GET':
        reg =Restaurant.objects.all()
        serializer =RestaurantSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400) 