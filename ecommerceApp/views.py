from operator import imod
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, userComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from  .models import product
from django.db.models import Q
from django import forms
from .models import comment
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form=UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'register.html', {'form':form})

@login_required(login_url='login/')
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

@login_required(login_url='/accounts/login/')
def productt(request):
    products=product.objects.all()
    return render(request, 'product.html', {'products':products})

@login_required(login_url='login/')
def productDetails(request,id):
    productss=product.objects.filter(id=id)
    return render(request, 'productDetails.html', {'productss':productss})

@login_required(login_url='login/')
def payment(request):
    return render(request, 'payment.html')
@login_required
def search(request):
    query=request.GET['query']
    search_view=product.objects.filter(ptype__icontains=query)
    return render(request, 'search.html', {'search_view':search_view})

@login_required
def comments(request,id):
    form = userComment(request.POST)
    if form.is_valid(id=id):
        form.save()
        return redirect('productDetails')
    else:
        form = userComment()
        return render(request, 'productDetails.html', {'form':form})