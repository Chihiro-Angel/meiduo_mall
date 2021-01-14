# -*- coding: utf-8 -*-
# author:yang  time:19-8-5 下午6:17


import logging

from celery_tasks.main import celery_app
from celery_tasks.sms import constants
from celery_tasks.yuntongxun.sms import CCP

logger = logging.getLogger("django")


@celery_app.task(name='send_sms_code')
def send_sms_code(mobile, sms_code):
    """
    发送短信验证码
    :param mobile: 手机号
    :param sms_code: 验证码时效
    :return: None
    """

    time = constants.SMS_CODE_EXPIRES
    try:
        ccp = CCP()
        ccp.send_template_sms(mobile, [sms_code, time], constants.SMS_CODE_TEMP_ID)
    except Exception as e:
        logger.error("发送验证码短信[异常][ mobile: %s, message: %s ]" % (mobile, e))
