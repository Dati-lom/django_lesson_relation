import http

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Item, Category



@api_view(["GET"])
def get_itme(request):
    print("CALLED")
    if request.method == "GET":
        data = Item.objects.get(id = 40).name

        return Response(data=data, status=http.HTTPStatus.OK) if data else Response(status=http.HTTPStatus.NOT_FOUND)

    return None

