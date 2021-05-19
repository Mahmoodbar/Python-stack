from django.shortcuts import render

def first(request):
    return render (request,"index1.html")

def result(request):
    name = request.POST['firstname']
    name2 = request.POST['lastname']
    location = request.POST['dojolocation']
    language = request.POST['favlanguage']
    option = request.POST['tex']

    
    context ={
        'name': name,
        'name2': name2,
        'location':location,
        'language':language,
        'option':option
    }
    print (context)
    return render (request,'result.html',context)