'''
Created on 23 Aug 2017

@author: i315244
'''
from __future__ import absolute_import, unicode_literals
import random
from websites.celery import app
from .models import Transaction

@app.task(name="sum_two_numbers")
def add(x, y):
    return x + y

@app.task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@app.task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)

@app.task(name="booking_trans")
def booking_transaction(booking_id):
    print(booking_id)
    Transaction.objects.create_trans(booking_id)
    