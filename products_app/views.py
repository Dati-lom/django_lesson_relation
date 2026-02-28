from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer, TagInputSerializer




@api_view(["GET", "POST"])
def items_view(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    # POST
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        # TODO: ensure create handles category_id and tag_ids
        item = serializer.save()
        return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def item_detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == "GET":
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            # TODO: ensure update handles category_id and tag_ids
            item = serializer.save()
            return Response(ItemSerializer(item).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def categories_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        category = serializer.save()
        return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def tags_view(request):
    serializer = TagInputSerializer(data=request.data)
    if serializer.is_valid():
        # TODO: implement tag creation in serializer
        tag = serializer.save()
        return Response({"id": tag.id, "name": tag.name}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
