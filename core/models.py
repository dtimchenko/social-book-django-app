from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

current_user = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(current_user, on_delete=models.CASCADE)
    id_user = models.IntegerField(blank=True)
    bio = models.TextField()
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.webp')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.get_username()
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(current_user, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    create_at = models.DateTimeField(default=datetime.now())
    no_of_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.get_username()
