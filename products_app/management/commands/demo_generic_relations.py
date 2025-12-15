from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from ...models  import Category, Item, Image

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        item = Item.objects.last()
        category = Category.objects.last()


        print(item.images.all())
        print(category.items.all())

        #გააკეთე ფოინთერი
        item_content_type = ContentType.objects.get_for_model(Item)

        item_images = Image.objects.filter(content_type=item_content_type, object_id=item.id)

        print(item_images)
