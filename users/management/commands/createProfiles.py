from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from users.models import Profile

class Command(BaseCommand):
    help = 'Links users with users profiles'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        profileCount = Profile.objects.count()
        userCount = User.objects.count()
        if userCount > profileCount:
            users = User.objects.all()
            profiles = Profile.objects.all()
            for user in users:
                if user.pk not in profiles.filter("user_id"):
                    profile = Profile()
                    profile.bio = ""
                    profiçe.user_id = user.pk

        else:
            print("The number of users and profiles is the same",file=self.sys.stdout)