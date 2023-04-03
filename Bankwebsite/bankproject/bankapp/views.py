from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from.models import District,branch

# Create your views here.
def getdata(request):
    deptcontext = District.objects.all()
    branchcontext = branch.objects.all()
    if request.method == 'POST':

        return redirect('/completed')

    return render(request, "profile.html", {'District': deptcontext, 'branch': branchcontext})


def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/new')
        else:
            messages.info(request, 'invalid login')
            return redirect('/login')

    return render(request, 'login.html')


def register(request ):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword= request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                return redirect('/login')

        else:
            messages.info(request, 'password miss match')
            return redirect('/register')
        return redirect('/login')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):
    if request.method=='POST':
        return redirect('/getdata')
    return render(request,"new.html")


def completed(request):
    return render(request, "completed.html")
