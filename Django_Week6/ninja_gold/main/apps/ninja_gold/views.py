# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from datetime import datetime

#Transaction and index

def index(request):   

    try:
        request.session['total']
    except KeyError:
        request.session['total']=0
    return render(request, 'ninja_gold/index.html')

def process(request,building):
    #Play Game process

    gold_play = 0    
    action = 'win' 
      
    if building == 'farm':
        gold_play = random.randrange(10,21)        
    elif building == 'cave':
        gold_play = random.randrange(5,11)          
    elif building == 'house':
        gold_play = random.randrange(2,6)        
    else:
        gold_play = random.randrange(-50,51)        
        #Win or lose   
        if gold_play < 0:
            action = 'lost'

    #timestamp for activities
    timestamp = datetime.now()

    #Activity Meassage key
    activity_log = {

            'class':action, 
            'message':"You {} {} golds from the {} ({})".format(action,abs(gold_play),building,timestamp)
    }

    try:
        log = request.session['logs']
    except KeyError:
        log = []

    #Add gold to total
    request.session['total'] += gold_play

    #Log gold into list
    log.append(activity_log)
    request.session['logs'] = log

    return redirect('/')        

def reset(request):
    request.session = 0

    return redirect('/')