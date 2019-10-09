from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from PIL import Image

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', 
        upload_to='profile_pics',
        blank=True,
        null=True)

    def __str__(self):
        return '{self.user.username} Profile'
       
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
