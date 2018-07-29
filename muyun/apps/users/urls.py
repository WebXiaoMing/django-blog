from django.conf.urls import re_path
from .views import getUserInfo

urlpatterns = [
    re_path(r'getUserInfo$', getUserInfo),
]