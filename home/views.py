from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from home.models import CustomUser,Sell
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
import random
# Create your views here.

def index(request):
    all_prod=list(Sell.objects.all())
    ran_prods=random.sample(all_prod,5)
    print(ran_prods)
    # if request.user.is_anonymous:
    #     return redirect('login')
    return render(request,'home/index.html',{'ran_prods':ran_prods})

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html') 

def buy(request,myid):
    prod=Sell.objects.get(id=myid)
    return render(request,'home/buy.html',{'product':prod})

def search(request):
    search=request.GET.get('search')
    # allprod=Sell.objects.filter(name='Car')
    allprod=Sell.objects.filter(name__icontains=search.casefold())
    print(allprod)
    print(search)
    # all_prod=list(Sell.objects.all())
    # ran_prods=random.sample(all_prod,3)
    # li=[i for i in allprod if i in search]
    # print(li)
    # for item in allprod:
    #     print(item.name)
    #     if item.name==search:
    #         return render(request,'home/index.html',{'ran_prods':ran_prods})
        
    return render(request,'home/search.html',{'allprod':allprod})

def sell(request):
    if request.method=="POST":
        name=request.POST['name'].lower()
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.POST['image']
        phone=request.POST['phone']
        sell=Sell(name=name,desc=desc,price=price,image=image,phone=phone)
        sell.save()
        messages.info(request,'Successfully Posted')
        return redirect('sell')
        return HttpResponse(request,'this is working')
    return render(request,'home/sell.html')
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return render(request, 'home/login.html')
    return render(request,'home/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']
        phone=request.POST['phone']
        password=request.POST['password']
        if len(username)<5:
            messages.info(request,'please enter a valid username')
        elif len(phone)<10:
            messages.info(request,'invalid mobile number')
        elif len(CustomUser.objects.filter(username=username))>1:
            messages.info(request,'username taken')
            return redirect('signup')
        elif len(CustomUser.objects.filter(phone=phone))>1:
            messages.info(request,'mobile number taken')
            return redirect('signup')
        else:
            user=CustomUser.objects.create_user(username=username,first_name=name,password=password,phone=phone)
            user.save()
    return render(request,'home/signup.html')

# def home(request):
#     # if request.user.is_anonymous:
#     #     return redirect('login')
#     return render(request,'home/index.html') 