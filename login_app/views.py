#from email.mime import image
#from http.client import HTTPResponse
from django.shortcuts import render
from login_app.forms import User_form,User_info_form
from login_app.models import User_Info
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from  django.contrib.auth.decorators import login_required
from django.urls import reverse

def login_page(request):
    dict={}
    return render (request,'login_app/login.html',context=dict)

def logged(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('login_app:index'))
                #return render(request,'login_app/login.html',context={})
                #return index(request)

            else:
                return HttpResponse("Account is not active")

        else:
            return HttpResponse("login details are wrong")
    else:
        return HttpResponseRedirect(reverse('loggin_app:user_login'))
        #return render(request,'login_app/login.html',context={})

@login_required
def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('login_app:index'))



def index(request):
    dict={}
    return render(request,'login_app/index.html',context=dict)


def register(request):
    registered=False
    if request.method=='POST':
        user_form=User_form(data=request.POST)
        user_info_form=User_info_form(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            User_Info=user_info_form.save(commit=False)
            User_Info.user=user

            if 'image' in request.FILES:
                User_Info.image=request.FILES['image']

            User_Info.save()
            registered=True
    else:
        user_form=User_form()
        user_info_form=User_info_form()

    dict={'us_form':user_form, 'us_info':user_info_form,'registered':registered}
    return render(request,'login_app/register.html',context=dict)