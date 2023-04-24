from django.db import models
from django.contrib.auth import get_user_model

current_user = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(current_user, on_delete=models.CASCADE)
    id_user = models.IntegerField(blank=True)
    bio = models.TextField()
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.webp')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.get_username()
    
