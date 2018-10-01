from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def index(request):
    return render(request, 'profile.html',{})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('students:login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
def logout_view(request):
    logout(request)
