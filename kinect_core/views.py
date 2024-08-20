from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .forms import SignUpForm, PhotoForm, ReelForm, SearchForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Photo
from .models import UserFollowing
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse

User = get_user_model()


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Succesfully")
                return redirect('home')
            else:
                messages.success(request, "Invalid username or password. Please try again.")
    else:
        form = LoginForm()

    return render(request, 'kinect_core/login.html', {
        'form': form
    })


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
    followed_users = UserFollowing.objects.filter(user_following=request.user).values_list('user_followed', flat=True)

    # User Following Photos
    photos_from_following = Photo.objects.filter(user__in=followed_users).order_by('-created_at')

    # Own Photos
    own_photos = Photo.objects.filter(user=request.user)

    # Combine the two
    photos = photos_from_following | own_photos
    photos = photos.order_by('-created_at')

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


@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    followers = user.followers.count()
    following = user.following.count()
    photos = Photo.objects.filter(user=user)
    is_following = UserFollowing.objects.filter(user_following=request.user, user_followed=user).exists()
    return render(request, 'kinect_core/profile.html', {
        'photos': photos,
        'user': user,
        'followers': followers,
        'following': following,
        'is_following': is_following,
    })


@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow != request.user:
        UserFollowing.objects.get_or_create(user_following=request.user, user_followed=user_to_follow)
    return redirect('profile', user_id=user_id)


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if request.user != user_to_unfollow:
        follow_object = UserFollowing.objects.filter(user_following=request.user, user_followed=user_to_unfollow)
        follow_object.delete()
    return redirect('profile', user_id=user_id)


def search(request):
    query = request.GET.get('query', '')
    results = []

    print(f"Received query: {query}")  # Debugging: Print the received query

    if query:
        results = User.objects.filter(
            username__icontains=query
        ) | User.objects.filter(
            first_name__icontains=query
        ) | User.objects.filter(
            last_name__icontains=query
        ) | User.objects.filter(
            email__icontains=query
        )

        print(f"Found {results.count()} results")  # Debugging: Print the number of results

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print("Processing AJAX request...")  # Debugging: Confirm AJAX request

        results_data = []
        for user in results:
            print(f"Processing user: {user.first_name} {user.last_name}")  # Debugging: Print each user processed

            user_data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_url': reverse('profile', args=[user.id])
            }
            results_data.append(user_data)

        print(
            f"Returning {len(results_data)} results in JSON")  # Debugging: Confirm the number of results being returned
        return JsonResponse({'results': results_data})

    print("Rendering search template")  # Debugging: Confirm template rendering
    return render(request, 'kinect_core/search.html', {
        'query': query,
        'results': results,
        'form': SearchForm(initial={'query': query}),
    })

def logout_user(request):
    logout(request)
    return redirect('login')
