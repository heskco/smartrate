from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from smartrate.models import Booking
from smartrate.serializer import BookingSerializer

from smartrate.tasks import booking_transaction

# Create your views here.
# smartrate/
class Bookings(APIView):
    
    def post(self, request):
        if request.method == 'POST':
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                booking = serializer.save()
                booking_id = booking.id
                booking_transaction.delay(booking_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
        
