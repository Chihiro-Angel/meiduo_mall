# -*- coding: utf-8 -*-
# author:yang  time:  下午3:22


from rest_framework.pagination import PageNumberPagination


class StandardPageNumPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    # 前端请求的每页数量上限
    max_page_size = 20
