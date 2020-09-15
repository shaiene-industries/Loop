from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from users.models import Profile

class Command(BaseCommand):
    help = 'Links users with users profiles'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        pCount = Profile.objects.count()
        uCount = User.objects.count()
        print("Profiles: {} Users: {}".format(pCount,uCount))
        if uCount > pCount:
            users = User.objects.exclude(profile__user__in=User.objects.all())
            for user in users:
                print("Creating profile for user: "+str(user))
                profile = Profile()
                profile.bio = ""
                profile.user = user
                profile.save()

        else:
            print("The number of users and profiles is the same")