from django.db import models
from django.utils import timezone

# Create your models here.
class user(models.Model):
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_picture_path = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class photo(models.Model):
    description = models.TextField()
    photo_path = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)


class comment_for_photo(models.Model):
    comment = models.TextField
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(user, on_delete=models.CASCADE)
    photoID = models.ForeignKey(photo, on_delete=models.CASCADE)

class photo_like(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(user, models.CASCADE)
    photoID = models.ForeignKey(photo, models.CASCADE)

class reel(models.Model):
    description = models.TextField()
    video_path = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(user, models.CASCADE)

class comment_for_reel(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(user, on_delete=models.CASCADE)
    reelID = models.ForeignKey(reel, on_delete=models.CASCADE)

class reel_like(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(user, models.CASCADE)
    reelID = models.ForeignKey(reel, models.CASCADE)

class user_following(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    userID = models.ForeignKey(user, related_name="following", on_delete=models.CASCADE)
    userID_following = models.ForeignKey(user, related_name="followers",on_delete=models.CASCADE)

class message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    userSenderID = models.ForeignKey(user, related_name="sent_message", on_delete=models.CASCADE)
    userReceiverID = models.ForeignKey(user, related_name="received_message",on_delete=models.CASCADE)


