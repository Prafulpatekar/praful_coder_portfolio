from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from praful_coder_portfolio.decorators import unauthenticated_user, allowed_users
from django.contrib import messages
from django.contrib.auth.models import Group,GroupManager,User
from portfolio.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


# @unauthenticated_user
def dashboardLogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            try:
                group = user.groups.get(name="MasterPraful")
                return redirect('dashboard')
            except Group.DoesNotExist:
                try:
                    group = user.groups.get(name="NormalUser")
                    return redirect('dashboardLogin')
                except Group.DoesNotExist:
                    messages.info(request,"username OR Password is incorrect ")
                    return redirect("dashboardLogin")
        else:
            messages.info(request,"username OR Password is incorrect ")
            return redirect("dashboardLogin")
    context={}
    messages.info(request,"login required ")
    return render(request ,'coderpanel/login.html',context)

def dashboardLogout(request):
    logout(request)
    messages.info(request,"You have successfully Logged Out")
    return redirect("dashboardLogin")

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def dashboard(request):
    return render(request,"coderpanel/dashboard.html")

### ABOUT SECTION TITLE START ###

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def showRoleName(request):
    roleNames = RoleNameModel.objects.all() 
    context = {"roleNames":roleNames}
    if request.method =="POST":
        roleName = request.POST.get('roleName')
        newRole,created= RoleNameModel.objects.get_or_create(roleName=roleName)
        return redirect("showRoleName")
    return render(request,"coderpanel/roleNameSection/showRoleName.html",context)

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def deleteRoleName(request,id):
    if request.method =="POST":
        role = RoleNameModel.objects.get(id=id)
        role.delete()
        messages.success(request,"Role deleted successfully!")
        return redirect("showRoleName")
    return redirect("showRoleName")

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def editRoleName(request,id):
    if request.method =="POST":
        role = RoleNameModel.objects.get(id=id)
        role.roleName = request.POST.get('roleName')
        role.save()
        messages.success(request,"Role updated successfully!")
        return redirect("showRoleName")
    return redirect("showRoleName")

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def activeRoleName(request,id):
    if request.method =="POST":
        role = RoleNameModel.objects.get(id=id)
        role.is_active = request.POST.get('is_active')
        role.save()
        messages.success(request,"Role status changed successfully!")
        return redirect("showRoleName")
    return redirect("showRoleName")

### ABOUT SECTION TITLE END ###


### ABOUT SECTION TITLE START ###

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def showAboutSectionTitle(request):
    titles = AboutSectionTitleModel.objects.all() 
    context = {"titles":titles}
    if request.method =="POST":
        titleName = request.POST.get('titleName')
        value = request.POST.get('value')
        rank = request.POST.get('rank')
        newtitle,created= AboutSectionTitleModel.objects.get_or_create(rank=rank,titleName=titleName,value=value)
        messages.success(request,"New title created successfully!")
        return redirect("showAboutSectionTitle")
    return render(request,"coderpanel/aboutSectionTitle/showAboutSectionTitle.html",context)

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def deleteAboutSectionTitle(request,id):
    if request.method =="POST":
        title = AboutSectionTitleModel.objects.get(id=id)
        title.delete()
        messages.success(request,"Title deleted successfully!")
        return redirect("showAboutSectionTitle")
    return redirect("showAboutSectionTitle")

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def editAboutSectionTitle(request,id):
    if request.method =="POST":
        title = AboutSectionTitleModel.objects.get(id=id)
        title.titleName = request.POST.get('titleName')
        title.rank = request.POST.get('rank')
        title.value = request.POST.get('value')
        title.save()
        messages.success(request,"Title updated successfully!")
        return redirect("showAboutSectionTitle")
    return redirect("showAboutSectionTitle")

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def activeAboutSectionTitle(request,id):
    if request.method =="POST":
        title = AboutSectionTitleModel.objects.get(id=id)
        title.is_active = request.POST.get('is_active')
        title.save()
        messages.success(request,"Title status changed successfully!")
        return redirect("showAboutSectionTitle")
    return redirect("showAboutSectionTitle")


### ABOUT SECTION TITLE END ###


### ABOUT SECTION TITLE START ###

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def showShortIntro(request):
    intros = ShortIntroModel.objects.all() 
    context = {"intros":intros}
    if request.method =="POST":
        introText = request.POST.get('introText')
        newIntro,created= ShortIntroModel.objects.get_or_create(introText=introText)
        return redirect("showShortIntro")
    return render(request,"coderpanel/shortIntro/showShortIntro.html",context)

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def deleteShortIntro(request,id):
    if request.method =="POST":
        intro = ShortIntroModel.objects.get(id=id)
        intro.delete()
        messages.success(request,"Short Intro deleted successfully!")
        return redirect("showShortIntro")
    return redirect("showShortIntro")

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def editShortIntro(request,id):
    if request.method =="POST":
        intro = ShortIntroModel.objects.get(id=id)
        intro.introText = request.POST.get('introText')
        intro.save()
        messages.success(request,"Short intro updated successfully!")
        return redirect("showShortIntro")
    return redirect("showShortIntro")

@login_required(login_url='dashboardLogin')
@allowed_users(allowed_roles=['MasterPraful'])
def activeShortIntro(request,id):
    if request.method =="POST":
        intros = ShortIntroModel.objects.filter()
        for i in intros:
            i.is_active = False
            i.save()
        role = ShortIntroModel.objects.get(id=id)
        role.is_active = True
        role.save()
        messages.success(request,"Role status changed successfully!")
        return redirect("showShortIntro")
    return redirect("showShortIntro")

### ABOUT SECTION TITLE END ###