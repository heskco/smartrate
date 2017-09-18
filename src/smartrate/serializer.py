'''
Created on 2 Aug 2017

@author: i315244
'''
from rest_framework import serializers
from smartrate.models import Booking 

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'
        