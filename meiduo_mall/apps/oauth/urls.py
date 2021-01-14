# -*- coding: utf-8 -*-
# author:yang  time:19-8-6 上午10:34
from django.conf.urls import url

from oauth import views

urlpatterns = [
    url(r'oauth/qq/authorization/$', views.QQAuthURLView.as_view()),
    url(r'oauth/qq/user/$', views.QQAuthURLView.as_view()),

]
