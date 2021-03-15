from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You Have Been Login !:)'))
            return redirect ('home')
        else:
            messages.success(request,('Error try to login again !:('))
            return redirect ('login')
    else:
        return render(request, 'stocks/login.html', {})

def logout_user(request):
    logout(request) 
    messages.success(request,('you have been successfully logout !!'))
    return redirect ('home')       

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+ ticker +"/quote?token=pk_aa6aeabd01a344969c515030915b44c5")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error...."
        return render(request, 'stocks/home.html', {'api':api})    

    else:
        return render(request, 'stocks/home.html', {'ticker': "enter a symbol above ...."})

    # pk_aa6aeabd01a344969c515030915b44c5

   


def about(request):
    return render(request, 'stocks/about.html', {})


def addstock(request):
    import requests
    import json
    if request.method == 'POST':
       form = StockForm(request.POST or None) 

       if form.is_valid():
           form.save()
           messages.success(request, ("Stock Has been Added !"))
           return redirect('addstock')

    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get(
                "https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) +"/quote?token=pk_aa6aeabd01a344969c515030915b44c5")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                    api = "Error...."

        return render(request, 'stocks/addstock.html', {'ticker':ticker, 'output':output})



def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Sold!"))
    return redirect ('sellstock')

def sellstock(request):
    ticker = Stock.objects.all()
    return render(request, 'stocks/sellstock.html', {'ticker':ticker})    



def mystock(request):
    return render(request, 'stocks/mystock.html', {})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('You Have Been register !:)'))
            return redirect ('home')

    else:
        form  = UserCreationForm() 

    context = {'form':form}    
    return render(request, 'stocks/register.html', context)
    

