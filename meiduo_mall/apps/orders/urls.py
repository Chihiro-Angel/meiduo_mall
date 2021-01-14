# -*- coding: utf-8 -*-
# author:yang  time: 19-8-14 上午9:12
from django.conf.urls import url

from orders import views

urlpatterns = [
    url(r'orders/settlement/$', views.OrderSettlementView.as_view()),
    url(r'orders/$', views.SaveOrderView.as_view()),
    # url(r'sms_codes/$', views.SMSCodeByTokenView.as_view()),
]