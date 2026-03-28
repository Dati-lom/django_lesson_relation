from django.urls import path
from . import views
from .views import ItemListView, ImageListView

urlpatterns = [
    path("items/", ItemListView.as_view(), name="items"),
    path("images/", ImageListView.as_view(), name="images"),

    path("items/<int:pk>/", views.item_detail_view, name="item_detail"),
    path("categories/", views.categories_view, name="categories"),
    path("tags/", views.tags_view, name="tags"),
]
