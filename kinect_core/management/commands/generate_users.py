from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Generate specified number of random users '

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help="Indicate the number of users to be randomly created")


    def handle(self, *args, **options):
        count = options['num_users']

        for i in range(0, count):
            User.objects.create_user(username=get_random_string(8), email=f"user_{i}@example.com", password="Itachi123")