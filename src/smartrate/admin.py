from django.contrib import admin

# Register your models here.
from .models import Booking
from .models import Hotel
from .models import Customer
from .models import Contract
from .models import Transaction

admin.site.register(Booking)
admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(Transaction)


