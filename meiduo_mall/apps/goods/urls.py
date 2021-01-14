# -*- coding: utf-8 -*-
# author:yang  time:  下午2:59


from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from goods import views

router = DefaultRouter()
router.register('skus/search', views.SKUSearchViewSet, base_name='skus_search')

urlpatterns = [
    url(r'categories/(?P<category_id>\d+)/hotskus/$', views.HotSKUListView.as_view()),
    url(r'categories/(?P<category_id>\d+)/skus?/$', views.SKUListView.as_view())
]

urlpatterns += router.urls