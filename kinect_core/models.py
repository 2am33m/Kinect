from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_picture_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Photo(models.Model):
    description = models.TextField()
    photo_path = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CommentForPhoto(models.Model):
    comment = models.TextField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PhotoLike(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    photo_id = models.ForeignKey(Photo, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reel(models.Model):
    description = models.TextField()
    video_path = models.TextField()
    user_id = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CommentForReel(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reel_id = models.ForeignKey(Reel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReelLike(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    reel_id = models.ForeignKey(Reel, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserFollowing(models.Model):
    user_followed = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, null=True)
    user_following = models.ForeignKey(User, related_name="following",on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message = models.TextField()
    userSenderID = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    userReceiverID = models.ForeignKey(User, related_name="receiver",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

