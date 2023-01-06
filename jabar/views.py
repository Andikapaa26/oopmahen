from django.shortcuts import render, redirect, HttpResponse
from .forms import KotaForm, PetaForm
from .models import Kota, Peta
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def index(request):
    data_kota = Kota.objects.all()
    data_peta = Peta.objects.all()
    data_peta_json = serializers.serialize('json', data_peta)
    konteks ={
        'dataJson':data_peta_json,
        'index':data_peta,
        'index': data_kota
    }
    return render(request, "jabar/index.html", konteks)



@login_required(login_url='login')
def list(request):
    konteks = {'list':Kota.objects.all(),}

    return render(request, "jabar/list.html", konteks)

@login_required(login_url='login')
def form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = KotaForm()
        else:
            kota = Kota.objects.get(pk=id)
            form = KotaForm(instance=kota)
        return render(request, "jabar/form.html", {'form':form})
    else:
        if id == 0:
            form = KotaForm(request.POST)
        else:
            kota = Kota.objects.get(pk=id)
            form = KotaForm(request.POST, instance=kota)
        if form.is_valid():
            form.save()
        return redirect('/jabar/list')

@login_required(login_url='login')
def hapus(request, id):
    kota = Kota.objects.get(pk=id)
    kota.delete()
    return redirect('/jabar/list')

@login_required(login_url='login')
def peta(request):
    data_peta = Peta.objects.all()
    data_peta_json = serializers.serialize('json', data_peta)
    konteks ={
        'dataJson':data_peta_json,
        'peta':data_peta
    }
    return render(request, "jabar/peta.html", konteks)

@login_required(login_url='login')
def formpeta(request, id=0):
    if request.method == "GET":
        if id==0:
            formpeta = PetaForm()
        else:
            peta = Peta.objects.get(pk=id)
            formpeta = PetaForm(instance=peta)
        return render(request, "jabar/formpeta.html", {'formpeta':formpeta})
    else:
        if id == 0:
            formpeta = PetaForm(request.POST)
        else:
            peta = Peta.objects.get(pk=id)
            formpeta = PetaForm(request.POST, instance=peta)
        if formpeta.is_valid():
            formpeta.save()
        return redirect('/jabar/peta')

@login_required(login_url='login')
def hapuspeta(request, id):
    peta = Peta.objects.get(pk=id)
    peta.delete()
    return redirect('/jabar/peta')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'jabar/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/jabar/list')
        else:
            return redirect ('/jabar/login')

    return render (request,'jabar/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('/jabar/login')


# Create your views here.
