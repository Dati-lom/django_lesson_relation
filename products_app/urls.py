from django.urls import path
from . import views

urlpatterns = [
    path("items/", views.items_view, name="items"),
    path("items/<int:pk>/", views.item_detail_view, name="item_detail"),
    path("categories/", views.categories_view, name="categories"),
    path("tags/", views.tags_view, name="tags"),
]
