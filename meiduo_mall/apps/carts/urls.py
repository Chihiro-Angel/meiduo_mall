# -*- coding: utf-8 -*-
# author:yang  time: 19-8-13 下午6:56
from django.conf.urls import url

from carts import views

urlpatterns = [
    url(r'cart/$', views.CartSerializer),
    # url(r'categories/(?P<category_id>\d+)/skus?/$', views.SKUListView.as_view())
]
