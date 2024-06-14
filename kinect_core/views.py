from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'kinect_core/login.html')
def signup(request):
    return render(request, 'kinect_core/signup.html')



