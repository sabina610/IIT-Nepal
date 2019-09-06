from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import HttpResponse

def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about\about.html')


def signup(request):
    return render(request,'signup.html')

def signin(request):
    if request.method=='GET':
        return render(request,'signin.html')
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'your password doesnt match')
            return redirect('signin')

@login_required(login_url='signin')
def dashboard(request):
    return render(request,'dashboard.html')


def signout(request):
    logout(request)
    return redirect('signin')


# def about(request):
#     context = {
#         'c' :  10,
#         'a' :[23,34,10]
#     }
#     return render(request,'about/about.html',context)



# def home(request):
#     return HttpResponse("<h1>Hello Nepal</h1>");


