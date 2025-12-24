from tkinter.constants import CASCADE
from unicodedata import category
from faker import Faker
from django.db import connection
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from ...models  import Category, Item, Image
from django.db import transaction

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        pass




