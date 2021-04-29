from rest_framework import routers, serializers, viewsets
from django.contrib.auth.hashers import make_password
from .models import * 

# create user

class UserRegistedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegisted
        fields = ('__all__')
        extra_kwargs = {'user': {'required':False}}

class RegistedSerializer(serializers.ModelSerializer):
    userregisted = UserRegistedSerializer(required=True) 
    class Meta:
        model = User
        fields= ('username','email','password','userregisted','first_name','last_name')

    def create(self, validated_data):
        insert = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            password = make_password(validated_data['password']),
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        register_data = validated_data.pop('userregisted')
        userregisted = UserRegisted.objects.create(
            user = insert,
            phone = register_data['phone'],
            gender = register_data['gender'],
        )
        return insert    
 
        fields=('__all__')  
        
          
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields=('__all__') 


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields=('__all__') 
        
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields=('__all__') 

class MokoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mokoro
        fields=('__all__') 

class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields=('__all__') 