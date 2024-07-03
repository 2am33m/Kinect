from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, PhotoForm, ReelForm
from django.contrib.auth.decorators import login_required
from .models import Photo


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Succesfully")
            return redirect('home')
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


def home(request):
    photos = Photo.objects.all()
    for photo in photos:
        print(f"Photo ID: {photo.id}, Photo Path: {photo.photo_path}")
    return render(request, 'kinect_core/home.html', {'photos': photos})



@login_required
def createPhoto(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        print(f"Form data: {request.POST}")
        print(f"Files data: {request.FILES}")
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, 'Photo posted successfully.')  # Set success message
            print("Form is valid. Redirecting...")
            return redirect('home')
        else:
            print("Sameem", form.errors)
            messages.error(request, 'Error posting photo. Please check the form.')  # Set error message
            print("Form is invalid. Rendering form again.")
    else:
        form = PhotoForm()

    print(f"Rendering form with initial data: {form.initial}")
    return render(request, 'kinect_core/create.html', {
        'form': form
    })
