from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/profile/{1}'.format(instance.user.id, filename)
    
class Profile(models.Model):
    """
    Extra user information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(help_text="Descreva-se com até 200 caracteres", blank=True,null=True, max_length=200)
    profile_image = models.ImageField(null=True, upload_to=user_directory_path)
    rank = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filenam
    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    def get_absolute_url(self):
        return reverse('users:other_user_account', kwargs={'pk':self.user.pk})

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
    
    def __str__(self):

        return str(self.user) + " | " + self.get_type_display()

# Create and update an instance of profile, after an User instance is saved
@receiver(post_save, sender=User) # Using a SIGNAl from user to profile
def create_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create and update an instance of ContactInfo, after an User instance is saved
@receiver(post_save, sender=User) # Using a SIGNAl from user to ContactInfo
def create_update_contact_info_email(sender, instance, created, **kwargs):
    if(created or not ContactInfo.objects.filter(user=instance).exists()):
        ContactInfo.objects.create(
            user=instance,
            type="EM",
            info=instance.email,
        )

    instance.profile.save()