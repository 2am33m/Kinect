from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Photo(models.Model):
    description = models.TextField()
    photo_path = models.ImageField(upload_to='posts/images', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentForPhoto(models.Model):
    comment = models.TextField(null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PhotoLike(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    photo_id = models.ForeignKey(Photo, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reel(models.Model):
    description = models.TextField()
    video = models.FileField(upload_to="posts/videos", null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentForReel(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reel_id = models.ForeignKey(Reel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReelLike(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    reel_id = models.ForeignKey(Reel, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserFollowing(models.Model):
    user_followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="followers", on_delete=models.CASCADE,
                                      null=True)
    user_following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE,
                                       null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    message = models.TextField()
    user_sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE)
    user_receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="receiver", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
