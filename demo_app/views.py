from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    data={
        "name":"disha",
        "age":20,
        "gender":"female",
        
    }
    #return HttpResponse("welcome")
    return render(request,"index.html",data)

def form(request):
    return render(request,"form.html")

"""def save_data(request):
    d1=DEMO()

    d1.fname=request.POST["fname"]
    d1.age=request.POST["age"]
    d1.marks=request.POST["marks"]

    d1.save()

    return redirect("index") """

"""def save_data1(request):
    d2=data()

    d2.fname=request.POST['fname']
    d2.lname=request.POST['lname']
    d2.marks=request.POST['marks']
    d2.per=request.POST['per']
    d2.save()

    return redirect("index")"""

def save_msg(request):
    d3=demo1()

    d3.fname=request.POST['fname']
    d3.lname=request.POST['lname']
    d3.age=request.POST['age']
    d3.gender=request.POST['gender']
    d3.save()

    return redirect("index")
