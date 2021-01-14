# -*- coding: utf-8 -*-
# author:yang  time:19-8-6 上午11:49
# from django.conf.urls import url
# from rest_framework.routers import DefaultRouter
# from areas import views
#
#
# router = DefaultRouter()
# router.register('areas', views.AreasViewSet, base_name='area')
# urlpatterns = [
#     url(r'areas/(?P<pk>\d+)/$', views.AreasViewSet.as_view()),
# ]
#
# urlpatterns += router.urls


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('areas', views.AreasViewSet, base_name='area')

urlpatterns = [
    # url('', include(router.urls))
]

urlpatterns += router.urls