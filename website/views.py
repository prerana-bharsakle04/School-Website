# Create your views here.
from django.http import HttpResponse
from website.models import *
from django.contrib import messages

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def act1(request):
    return render(request,'act1.html')

def act2(request):
    return render(request,'act2.html')

def act3(request):
    return render(request,'act3.html')

def act4(request):
    return render(request,'act4.html')

def act5(request):
    return render(request,'act5.html')

def act6(request):
    return render(request,'act6.html')

def contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('subject')
        d = request.POST.get('message')
        enquiry = enquiry_table(name = a, email = b, subject = c, message = d)
        enquiry.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...')
    return render(request,'contact.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # is not None is keyword None 'N' is capital which check above user (username and password) is available in database or not

            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
            # from django.shortcuts import redirect, render - this module we need to import in same file, to access redirect() where only path name should be call
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')    
        
    return render(request, 'login.html')

def dashboard(request):
    return render(request,'dashboard.html')
