from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    return render(request,"portfolio/index.html")

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        newMessage = ContactModel(
            name=name,
            email=email,
            subject=subject,
            message=message,

        )
        newMessage.save()
        return redirect("index")
    return redirect("index")