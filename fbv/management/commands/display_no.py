from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('start', type=int, help='Indicates from which number to start printing')
        parser.add_argument('end', type=int, help='Indicates from which number to start printing')

    def handle(self, *args, **kwargs):
        start = kwargs['start']
        end = kwargs['end']
        for i in range(start,end+1):
            print(i)