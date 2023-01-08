from django.db import models
from django.contrib.auth.models import User
from project.userapp.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.


class message(models.Model):
    # user = models.OneToOneField(Profile, on_delete=models.CASCADE, null = True, blank=True)
    first_name = models.CharField(max_length=25, null=True, blank=True, unique=False)
    last_name = models.CharField(max_length=25, null=True, blank=True, unique=False)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=False)
    messages = models.CharField(max_length=200, null=True, blank=True, unique=False)



# def user_directory_path(instance, filename):
#     return f'user_{0}/{1}'.format(instance.user.id, filename)
class uploadIdea(models.Model):
    reason = [
        ('Selling','Selling'),
        ('Investing','Investing'),
    ]

    wort = [
        ('$0-$100','$0-$100'),
        ('$100-$1000','$100-$1000'),
        ('$1000-$10000','$1000-$10000'),
        ('$10000 above','$1000 above'),
    ]

    fileToUpload = models.FileField(upload_to = 'ideas/', null = True,)
    purpose = models.CharField(max_length=20, null=False, unique=False, choices=reason)
    worth = models.CharField(max_length=20, unique=False, null=False, choices=wort)
    pincode = models.CharField(max_length=6, unique=False, null=False)
    email = models.EmailField(max_length=50, unique=False, null=True, blank=True)
    user_id = models.CharField(max_length=200, unique=False, null=False)
    status = models.BooleanField(unique=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null =False)
    description = models.CharField(max_length=225, null=False, blank=False,unique=False)
    payment = models.CharField(max_length=20, null=True, unique=False, blank=True)

class bugsModel(models.Model):
    global bugs
    bugs = [('Social Media Bug','Social Media Bug'),
    ('Nigeria BankApp Bugs','Nigeria BankApp Bugs'),
    ('Apple Device Bugs','Apple Device Bugs'),
    ('Android Device Bugs','Android Device Bugs'),
    ('Tech bugs', 'Tech bugs'),
    ('General bugs', 'General bugs'),

    # ('others (please specify)', 'others (please specify)')
]
    
    bank = [
   
            ('Facebook Bugs', 'Facebook Bugs'),
            ('Instagram Bugs', 'Instagram Bugs'),
            ('Twitter Bugs', 'Twitter Bugs'),
            ('Snapchat Bugs', 'Snapchat Bugs'),
            ('Tiktok Bugs', 'Tiktok Bugs'),
            ('Whatsapp Bugs', 'Whatsapp Bugs'),
            ('', ''),
        ('Zenith Bank', 'Zenith Bank'),
        ('UBA Bank', 'UBA Bank'),
        ('GT Bank', 'GT Bank'),
        ('Access Bank', 'Access Bank'),
        ('Wema Bank', 'Wema Bank'),
        ('', ''),
        ('Iphone', 'Iphone'),
        ('MACBOOK', 'MACBOOK'),
        ('Apple Watch', 'Apple Watch'),
        ('', ''),
        ('Android phone', 'Android phone'),
        # ('', ''),
        ('others(please specify)', 'others(please specify)'),

            ]
     


    bug_type = models.CharField(choices=bugs ,max_length=30, null=False, unique=False, blank=False)
    bug_name = models.CharField(choices=bank, max_length=30, null=False, unique=False, blank=False)
    email = models.CharField(max_length=50, null=False, unique=False, blank=False)
    description = models.CharField(max_length=225, null=False, unique=False, blank=False)
