# -*- coding: utf-8 -*-
# author:yang  time:19-8-6 上午11:48


from rest_framework import serializers

from areas.models import Area


class AreaSerialier(serializers.ModelSerializer):
    """行政区域信息序列化器"""

    class Meta:
        model = Area
        fields = ('id', 'name')


class SubAreaSerializer(serializers.ModelSerializer):
    """
    子级行政区划信息
    """
    subs = AreaSerialier(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')
