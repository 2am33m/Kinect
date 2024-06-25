from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect()
        else:
            messages.success(request, "There was an error logging In, Try again...")
            return redirect("login")
    else:
        return render(request, 'kinect_core/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=email, password=password)
            messages.success(request, "Account created successfully")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'kinect_core/signup.html', {
        'form': form
    })


7
