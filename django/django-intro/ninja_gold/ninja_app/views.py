from django.shortcuts import redirect, render
import random
from datetime import datetime

def first(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold']=0
        request.session['activities']=[]

    return render (request,'index.html')
    

def second(request):
    if request.method == 'POST':
        if request.POST['building'] == 'cave':
            x= random.randint(5,10)
            request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['building'] =='Farm':
            x = random.randint(10,20)
            request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['building'] =='House':
            x = random.randint(2,5)
            request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['building'] =='Casino':
            x = random.randint(-50,50)
            if x >0:
                request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            if x<0:
                request.session['activities'].append('You have lost ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
    request.session['gold'] += x
       
    return redirect('/')