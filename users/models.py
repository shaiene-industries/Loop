from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    """
    Extra user information
    """
    full_name = models.CharField(verbose_name = "Nome completo",max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

# These functions will create and update an instance of profile, after an User instance is saved
@receiver(post_save, sender=User) # Using a SIGNAl from user to profile
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveUserProfile(sender, instance, **kwargs):
    instance.profile.save()