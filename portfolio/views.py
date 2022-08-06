import imp
from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    roles = RoleNameModel.objects.filter(is_active=True)
    titles = AboutSectionTitleModel.objects.filter(is_active=True)
    intros = ShortIntroModel.objects.get(is_active=True)
    context = {"roles":roles,"titles":titles,"intros":intros}
    return render(request,"portfolio/index.html",context)

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
        mysub= "Would you like more information?"
        mymsg = f"Hi {name},\nThank you for contacting me!If you’re looking for a web designer to reconstruct your business website or need to develop a web application for your buisness, then you can hire me.\nI’ve worked with a lot of great brands and small businesses over the past 1 years.\nYou can check out some of my work on my portfolio at https://praful-coder-portfolio.herokuapp.com/. If you’re interested, I’d love to discuss more details.\n\n\n\nKind regards,\nPraful Patekar"
        send_mail(
            mysub,
            mymsg,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        return redirect("index")
    return redirect("index")