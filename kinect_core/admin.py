from django.contrib import admin
from .models import Photo, CommentForPhoto, PhotoLike, Reel, CommentForReel, ReelLike, UserFollowing, Message
# Register your models here.

admin.site.register(Photo)
admin.site.register(CommentForPhoto)
admin.site.register(PhotoLike)
admin.site.register(Reel)
admin.site.register(CommentForReel)
admin.site.register(ReelLike)
admin.site.register(UserFollowing)
admin.site.register(Message)

