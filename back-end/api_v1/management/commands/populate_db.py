from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from api_v1.models import Category, Permission, Role, User


class Command(BaseCommand):
    """_summary_

    Args:
        BaseCommand (_type_): _description_
    """

    def add_arguments(self, parser):
        parser.add_argument(
            'total', type=int, help='Indicates the number of each model to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            Category.objects.create(
                name=get_random_string(10), description=get_random_string(10))
            Permission.objects.create(
                name=get_random_string(10), description=get_random_string(10))
            Role.objects.create(name=get_random_string(10),
                                description=get_random_string(10))
            User.objects.create(username=get_random_string(10
                                                           ), email=f'{get_random_string(10)}@test.com', password=get_random_string(16))
        self.stdout.write(self.style.SUCCESS('Data created successfully'))
