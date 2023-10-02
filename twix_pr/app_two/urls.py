from django.urls import re_path
from . import views

app_name = 'app_two'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<product_id>[0-9]+)/$', views.detail, name='product_detail'),
]