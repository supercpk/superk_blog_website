from django.urls import path
from django.urls import re_path  #正则表达式
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.index, name='blog_index'), # http:....
    re_path(r'^(?P<blog_id>[0-9]+)', views.detail, name='blog_detail'),
    re_path(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='blog_category'),
    re_path(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name='blog_tag'),
    re_path(r'^search/$', views.search, name='blog_search'),#搜索
    re_path(r'^reply/(?P<comment_id>\d+)/$', views.reply, name='comment_reply'),
    re_path(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name='blog_archives'),
    # path('?P<blog_id>[0-9]+', views.detail, name='blog_detail'),# 正则表达式的新用法

]
