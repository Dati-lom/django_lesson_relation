from django.urls import path
from . import views

urlpatterns = [
    # path('items/', views.list_items, name='list_items'),
    # path('items/<int:pk>/', views.item_detail, name='item_detail'),
    # path('categories/', views.list_categories, name='list_categories'),
    #
    path("item/", views.get_itme, name="items")
]

