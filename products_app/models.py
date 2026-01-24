import datetime

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Image(models.Model):
    url = models.CharField(max_length=255)

    #რომელს უყურებს
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #კონკრეტულად რას უყურებს
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    #
    # tag_fk = models.ForeignKey()
    # category_fk = models.ForeignKey()
    # item_fk = models.ForeignKey()


    def __str__(self):
        return self.url



class CustomManager(models.Manager):

    def get_by_name(self,name):
        return super().filter(name=name).first()

    def custom_query(self, table_name):
        return self.raw(f"SELECT * FROM {table_name}")


    def filter(self, *args, **kwargs):
        data = super().filter(*args, **kwargs)
        print(f"FILTERED NOW AT {datetime.date.today()}")
        return data
class Category(models.Model):
    name = models.CharField(max_length=100)
    images = GenericRelation(Image)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    tags = models.ManyToManyField(Tag, related_name='items')
    images = GenericRelation(Image)
    active = models.BooleanField()



    def __str__(self):
        return self.name
