from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_user, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
    path('create/', views.createPhoto, name='create'),
    path('profile/<int:user_id>', views.profile_view, name='profile'),
    path('follow/<int:user_id>', views.follow_user, name='follow'),
    path('unfollow/<int:user_id>', views.unfollow_user, name='unfollow'),
    path('search/', views.search, name='search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
