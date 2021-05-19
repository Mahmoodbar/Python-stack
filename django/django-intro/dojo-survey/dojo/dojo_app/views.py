from django.shortcuts import render

def first(request):
    return render (request,"index1.html")

def result(request):
    return render (request,"index.html")