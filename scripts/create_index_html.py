# -*- coding: utf-8 -*-
# author:yang  time:19-8-6 下午5:24


import sys
import os
import django
from contents.crons import generate_static_index_html


sys.path.insert(0, '../')
sys.path.insert(0, '../meiduo_mall/apps')


if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'

# 让django进行初始化设置

django.setup()


if __name__ == '__main__':
    generate_static_index_html()
