import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Tags, Categories, Years, Blogs, Detail

# Create your views here.


# 获取所有博客详情
@require_http_methods(["GET"])
def getBlogDetail(request):
    response = {}
    id = request.GET.get('id')
    try:
        detail = Detail.objects.filter(blog=id)
        response['data'] = json.loads(serializers.serialize("json", detail))
        response['code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


# 获取所有标签
@require_http_methods(["GET"])
def getTagList(request):
    response = {}
    tags = Tags.objects.all()
    try:
        response['data'] = json.loads(serializers.serialize("json", tags))
        response['code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


# 获取所有博客数
@require_http_methods(["GET"])
def getBlogList(request):
    response = {}
    blogs = Blogs.objects.order_by('-add_time')
    lens = len(blogs)
    page = request.GET.get('page', 1)
    pageNum = request.GET.get('pageNum')
    paginator = Paginator(blogs, pageNum)

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    try:
        response['data'] = json.loads(serializers.serialize("json", contacts))
        response['num_pages'] = paginator.num_pages
        response['code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)

