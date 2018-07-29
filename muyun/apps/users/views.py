import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers

from .models import UserProfile


# 获取用户信息
@require_http_methods(["GET"])
def getUserInfo(request):
    response = {}
    name = request.GET.get('name')
    user = UserProfile.objects.filter(username=name)
    try:
        response['data'] = json.loads(serializers.serialize("json", user))
        response['code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


