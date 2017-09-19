'''
Created on 23 Aug 2017

@author: i315244
'''
from __future__ import absolute_import, unicode_literals
from websites.celery import app
from .models import Transaction

@app.task(name="booking_trans")
def booking_transaction(booking_id):
    print(booking_id)
    Transaction.objects.create_trans(booking_id)
    