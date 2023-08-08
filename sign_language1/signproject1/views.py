from contextlib import redirect_stderr
import email
from fileinput import filename
from urllib import request
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
import os
import sys
import subprocess

# Create your views here.

def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        name1=request.POST.get('name1')
        addr=request.POST.get('addr')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        phone1=request.POST.get('phone1')
        email1=request.POST.get('email1')
        pass1=request.POST.get('pass1')    
        registermodel(name1=name1,addr=addr,dob=dob,age=age,phone1=phone1,email1=email1,pass1=pass1).save()
        return redirect('login')
    else:        
     return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def log(request):
    if request.method=="POST":
        email1= email1=request.POST.get('email1')
        pass1=request.POST.get('pass1')    

        cr=registermodel.objects.filter(email1=email1,pass1=pass1)
        if cr:
            user=registermodel.objects.get(email1=email1,pass1=pass1)
            email1=user.email1
            pass1=user.pass1
            request.session['email']=email1
            request.session['pass1']=pass1
            return redirect('home')
        else:    
            return render(request,'login.html')
    else:
        return render(request,'register.html')        

def home(request):
    return render(request,'home.html')     

def file(request):

    command='python C:\\Users\\sreel\\Desktop\\sign\\Sign-Language-Detector-main\\SignDetector.py'
    os.system(command)

    return render(request,'file.html')     


def view(request):
    cr=registermodel.objects.all()
    return render(request,"view.html",{'cr':cr})

def delete(request,pk):
    cr=registermodel.objects.get(id=pk)
    cr.delete()
    return redirect("view")      