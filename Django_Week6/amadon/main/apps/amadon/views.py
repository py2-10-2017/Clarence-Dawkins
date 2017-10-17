# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#Bring items from products.py
from products import items

#Transaction and index

def index(request):
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']

    products =  {
        "items":items
    }
    return render(request, 'amadon/index.html', products)

def buy(request,item_id):

    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    try:
        request.session['total_price']
    except KeyError:
        request.session['total_price']=0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items']=0

    request.session['total_price'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    
    return redirect('/checkout')

def checkout(request):

    return render(request, 'amadon/checkout.html')

