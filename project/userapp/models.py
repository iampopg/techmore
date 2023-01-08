from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    idea = [
        ("Business Idea","Business Idea"),
        ("Tech Idea","Tech Idea")
    ]
    pat = [
        ('Selling','Selling'),
        ('Investing','Investing')
    ]
    gend =[
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
        ('Not prefer to say','Not prefer to say'),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="profileImage/", unique = False, null=True)
    idea_type = models.CharField(choices=idea, max_length=100, null= True)
    purpose = models.CharField(choices=pat, max_length=100, null=True)
    DOB = models.DateTimeField(unique=False, max_length=10, null=True)
    address = models.CharField(unique=False, max_length=80, null=True)
    gender = models.CharField(choices=gend, max_length=30, null=True, unique=False, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=False, unique=False)
    staff = models.BooleanField(default = False, unique= False)

    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
            
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):    
     instance.profile.save()
