from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from api_v1.models import User

# Create your views here.


def users_list(request):
    users = User.objects.all()
    users_json = serializers.serialize('json', users)
    return JsonResponse(users_json, safe=False)
