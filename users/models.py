from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    """
    Extra user information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(help_text="Descreva-se com até 200 caracteres", blank=True,null=True, max_length=200)

class ContactInfo(models.Model):
    """
    Information about each contact method
    """
    CONTACT_TYPE_CHOICES = [
        ("CP", "Celular"),
        ("FB", "Facebook"),
        ("IG", "Instagram"),
        ("TT", "Twitter"),
        ("TG", "Telegram"),
        ("EM", "E-mail"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=CONTACT_TYPE_CHOICES, help_text="Nome do meio de contato")
    info = models.CharField(max_length=50)

# Create and update an instance of profile, after an User instance is saved
@receiver(post_save, sender=User) # Using a SIGNAl from user to profile
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
