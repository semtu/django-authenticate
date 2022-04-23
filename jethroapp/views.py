from django.shortcuts import render
from .forms import model_form,user_form,profile_form
from .models import form_model,user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'jethroapp/index.html',{})

def form_view(request):
    Form=False
    display=form_model.objects.order_by('first_name')
    if request.method=='POST':
        formview=model_form(request.POST)
        if formview.is_valid():
            formview.save(commit=True)
            # return index(request)
            Form=True
        else:
            print(formview.errors)
    else:
        formview=model_form()
    return render(request,'jethroapp/form.html',{'formview':formview, 'Form':Form, 'display':display})

def register(request):
    Registered=False
    display=user_model.objects.order_by('user_id')
    if request.method=='POST':
        userview=user_form(request.POST)
        profileview=profile_form(request.POST,request.FILES)
        if userview.is_valid() and profileview.is_valid():
            user=userview.save()
            user.set_password(user.password)
            user.save()

            profile=profileview.save(commit=False)
            profile.user=user
            profile.save()

            Registered=True
        else:
            print('form is invalid')
    else:
        userview=user_form()
        profileview=profile_form()
    return render(request,'jethroapp/signup.html',{'userview':userview,'profileview':profileview,'Registered':Registered,'display':display})

def logins(request):
    logged=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                logged=True
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed')
            return HttpResponse('Invalid login details')

    else:
        return render(request, 'jethroapp/login.html',)

@login_required
def logouts(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in")