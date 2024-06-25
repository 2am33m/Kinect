from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
