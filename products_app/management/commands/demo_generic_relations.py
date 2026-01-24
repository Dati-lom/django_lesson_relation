from tkinter.constants import CASCADE
from unicodedata import category
# from faker import Faker
from django.db import connection
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from ...models  import Category, Item, Image
from django.db import transaction

class Command(BaseCommand):


    def handle(self, *args, **kwargs):


        content_type = ContentType.objects.get_for_model(Category)

        #create
        category = Category.objects.create(name="cat")
        category2 = Category(name="TEST")
        category.save()

        with transaction.atomic():
            cat = Category.objects.filter(id=1)
            cat.update(name="test")
            cat_to_delete = Category.objects.filter(id=2)
            cat_to_delete.delete()

        Category.objects.filter(name="TEST").update(name="TEST2")


        print(f"content type {content_type}")




