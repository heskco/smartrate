from django.db import models
from random import choices
import datetime

# Create your models here.
class Booking(models.Model):
    reserv_id = models.CharField(max_length=50)
    guest_name = models.CharField(max_length=100)
    client_id = models.CharField(max_length=50)
    hotel_id = models.CharField(max_length=50)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    corp_ref = models.CharField(max_length=50)
    
    def __str__(self):
        return self.reserv_id
    
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    hotel_id = models.CharField(max_length=30)
    account_id = models.CharField(max_length=30)
        
    def __str__(self):
        return self.hotel_name    
        
    def fullname(self):
        return '{} {}'.format(self.group_name, self.hotel_name)

class Customer(models.Model):
    cust_name = models.CharField(max_length=100)
    cust_addr = models.CharField(max_length=150)
    cust_id = models.CharField(max_length=30)
    account_id = models.CharField(max_length=30)
    
    def __str__(self):
        return self.cust_name
    
class Contract(models.Model):
    hotel = models.ForeignKey(Hotel,
                    on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer,
                    on_delete = models.CASCADE)                
    currency = models.CharField(max_length=5)
    base_rate = models.DecimalField(max_digits=6,decimal_places=2)
    PAY_FREQUENCY_CHOICES = (
        ('0', 'Daily'),
        ('1', 'Weekly'),
        ('2', 'Monthly'),
    )
    COMM_RATE_CHOICES = (
        ('0', 'Amount'),
        ('1', 'Percentage'),   
    )
    pay_freq = models.CharField(max_length=1, choices=PAY_FREQUENCY_CHOICES)
    commission_type = models.CharField(max_length=1, choices=COMM_RATE_CHOICES, )
    comission = models.CharField(max_length=5)
    
    def __str__(self):
        return '{} {}'.format(self.hotel.hotel_name, self.customer.cust_name)
        
class TransManager(models.Manager):
    def create_trans(self, booking_id):
        booking = Booking.objects.get(pk=booking_id)
        
        start = booking.arrival_date
        end = booking.departure_date
        delta = (end-start).days
        print(delta)
        
        hotel = Hotel.objects.get(hotel_id=booking.hotel_id)
        print(hotel.hotel_name)
        client = Customer.objects.get(cust_id=booking.client_id)
        print(client.cust_name)
        
        contracts = Contract.objects.filter(customer=client.id)
        
        print(contracts.count())
        
        for x in contracts:
            
            if x.hotel.id == hotel.id:
                self.contract = x
                self.value = (x.base_rate * delta)
                self.comission = 200
                break
                
        
        self.booking = booking
        
        self.trans_date = datetime.datetime.now()
        
        transaction = self.create(contract=self.contract, booking=self.booking, value=self.value,
                                  comission=200, trans_date=self.trans_date)
        return transaction

class Transaction(models.Model):
    contract = models.ForeignKey(Contract,
                    on_delete = models.CASCADE)
    booking = models.ForeignKey(Booking,
                    on_delete = models.CASCADE)                
    value = models.DecimalField(max_digits=8,decimal_places=2)
    comission = models.DecimalField(max_digits=6,decimal_places=2)
    trans_date = models.DateTimeField()
    
    def __str__(self):
        return '{} {} {}'.format(self.booking.reserv_id, self.value, self .trans_date)
    
    objects = TransManager()   
        
        
    
    
                