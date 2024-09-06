import requests
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User



class Command(BaseCommand):
    help = 'Generate specified number of random users fetched from the internet'

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help="Indicate the number of users to be randomly created")

    def fetch_random_users(self, count):
        """Fetch random users data from randomuser.me API"""
        url = f'https://randomuser.me/api/?results={count}&nat=us'
        response = requests.get(url)
        data = response.json()

        users = []
        for user_data in data['results']:
            user_info = {
                'username': user_data['login']['username'],
                'email': user_data['email'],
                'first_name': user_data['name']['first'],
                'last_name' : user_data['name']['last'],
            }
            users.append(user_info)

        return users

    def handle(self, *args, **options):
        num_users = options['num_users']
        batch_size = 100 # Fetch and create users in small batches to avoid overflowing API
        for i in range(0, num_users, batch_size):
            current_batch_size = min(batch_size, num_users - i)
            random_users = self.fetch_random_users(current_batch_size)

            # Create user instance
            users = []
            for user in random_users:
                user_instance = User(
                    username=user['username'],
                    email=user['email'],
                    first_name=['first_name'],
                    last_name=['last_name'],
                    password='Itachi123', # Set a default Password
                )
                users.append(user_instance)

            #Save the user in bulk
            User.objects.bulk_create(users)
            self.stdout.write(f'{i + current_batch_size} users created successfully')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_users} users'))


