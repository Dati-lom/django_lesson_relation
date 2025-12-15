import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from products_app.models import Category, Tag, Item

def populate():
    # Clear existing data
    Item.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()

    # Create Categories
    sport = Category.objects.create(name="Sport")
    toys = Category.objects.create(name="Toys")
    electronics = Category.objects.create(name="Electronics")

    # Create Tags
    sale = Tag.objects.create(name="Sale")
    new = Tag.objects.create(name="New")
    old = Tag.objects.create(name="Old")

    # Create Items
    # 1. Item > 100 (for Tag query)
    item1 = Item.objects.create(name="Expensive Sport Item", price=150, category=sport)
    item1.tags.add(sale)

    # 2. Item > 50 and category "sport"
    item2 = Item.objects.create(name="Cheap Sport Item", price=60, category=sport)
    item2.tags.add(new)

    # 3. Item < 50 and category "toys" and tag "sale" or "new"
    item3 = Item.objects.create(name="Toy Car", price=40, category=toys)
    item3.tags.add(sale)

    item4 = Item.objects.create(name="Toy Doll", price=30, category=toys)
    item4.tags.add(new)

    item5 = Item.objects.create(name="Toy Block", price=45, category=toys)
    item5.tags.add(old) # Should not match the filter

    item6 = Item.objects.create(name="Laptop", price=1000, category=electronics)
    item6.tags.add(new)

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()

