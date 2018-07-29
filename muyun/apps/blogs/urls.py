from django.conf.urls import re_path
from .views import getBlogDetail, getBlogList, getTagList

urlpatterns = [
    re_path(r'getBlogDetail$', getBlogDetail),
    re_path(r'getBlogList$', getBlogList),
    re_path(r'getTagList$', getTagList),
]