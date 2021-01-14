# -*- coding: utf-8 -*-
# author:yang  time:19-8-6 上午10:31
from urllib.parse import parse_qs
from urllib.request import urlopen

from django.utils.http import urlencode

from celery_tasks.sms.tasks import logger
from meiduo_mall.settings import dev
from .exceptions import QQAPIException


class OAuthQQ(object):
    """
    用户QQ登陆工具类
    """

    def __init__(self, app_id=None, app_key=None, redirect_url=None, state=None):
        self.app_id = app_id or dev.QQ_APP_ID
        self.app_key = app_key or dev.QQ_APP_KEY
        self.redirect_url = redirect_url or dev.QQ_REDIRECT_URL
        self.state = state or dev.QQ_STATE

    def generate_qq_login_url(self):
        """
        拼接用户QQ登录的链接地址
        :return: 链接地址
        """
        url = 'https://graph.qq.com/oauth2.0/authorize?'
        data = {
            'response_type': 'code',
            'client_id': self.app_id,
            'redirect_uri': self.redirect_url,
            'state': self.state,
            # 获取用户的qq的openid
            'scope': 'get_user_info'
        }
        query_string = urlencode(data)
        url += query_string
        print(url)

        return url

    def get_access_token(self, code):
        """
        获取qq的access_token
        :param code: 调用的凭据
        :return: access_token
        """
        url = 'https://graph.qq.com/oauth2.0/token?'
        req_data = {
            'grant_type': 'authorization_code',
            'client_id': self.app_id,
            'client_secret': self.app_key,
            'code': code,
            'redirect_uri': self.redirect_uri
        }

        url += urlencode(req_data)

        try:
            # 发送请求
            response = urlopen(url)
            # 读取QQ返回的响应体数据
            # access_token=FE04************************CCE2&expires_in=7776000&refresh_token=88E4************************BE1
            response = response.read().decode()

            # 将返回的数据转换为字典
            resp_dict = parse_qs(response)

            access_token = resp_dict.get("access_token")[0]
        except Exception as e:
            logger.error(e)
            raise QQAPIException('获取access_token异常')

        return access_token
