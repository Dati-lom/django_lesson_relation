from django.shortcuts import render, get_object_or_404
from .models import Item, Category

def list_items(request):
    # TODO: Optimize this query using select_related and prefetch_related
    # We want to fetch all items with their category, tags, and images.
    # Currently, this will cause N+1 problem in the template if we access related fields.
    # Hint: Use select_related for ForeignKey (category)
    # Hint: Use prefetch_related for ManyToMany (tags) and GenericRelation (images)
    items = Item.objects.all()

    return render(request, 'products_app/item_list.html', {'items': items})

def item_detail(request, pk):
    # TODO: Optimize this query to fetch the item with its related data efficiently
    # Hint: You can chain select_related and prefetch_related
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'products_app/item_detail.html', {'item': item})

def list_categories(request):
    # TODO: Optimize this query. We want all categories and their related items.
    # Hint: Use prefetch_related for Reverse ForeignKey (items)
    categories = Category.objects.all()
    return render(request, 'products_app/category_list.html', {'categories': categories})
