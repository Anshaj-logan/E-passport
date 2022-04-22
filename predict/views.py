from django.shortcuts import render,redirect
from predict.forms import UserForm, UserForm1


from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
# Create your views here.


def view(request):
    return render(request, "home.html")

def admin(request):
    return render(request, "admin.html")

def user(request):
    return render(request, "user.html")

def userview(request):
    return render(request, "userview.html")

def aboutview(request):
    return render(request, "about.html")





def add_det(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = UserForm()
    return render(request, 'adddetails.html', {'form':form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('admin')
        else:
            pass
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def siup(request):
    
    if request.method == 'POST':
        frm = UserForm1(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('user')
    else:
        frm = UserForm1()
    return render(request, 'siup.html', {'frm':frm})
    


def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('userview')
        else:
            pass
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'slog.html', context)