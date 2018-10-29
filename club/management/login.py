from .verify import gene_code
from .utils import *
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
import os


def __save_session(**kwargs):
    sessionStore = SessionStore()
    # if 'iden_code' in kwargs:
    #     sessionStore['iden_code'] = kwargs['iden_code']
    # if 'user_name' in kwargs:
    #     sessionStore['user_name'] = kwargs['user_name']
    for key in kwargs.keys():
        sessionStore[key] = kwargs[key]
    sessionStore.save()
    session_key = sessionStore.session_key
    return session_key


def __read_session(session_key):
    session = Session.objects.get(pk=session_key)
    # print(session.session_data)  # 返回session的存储（加密过）
    return session.get_decoded()  # 返回session的数据结构（加过解码）
    # print(session.expire_date)


def login_page(request):
    try:
        temp_dict = {}
        temp_dict = gene_code()
        session_key = __save_session(iden_code=temp_dict['text'], pic_url=temp_dict['pic_url'])
        data = {}
        data['pic_url'] = temp_dict['pic_url']
        data['session_key'] = session_key
        return JsonResponse({'status': 0, 'data': data})
    finally:
        os.remove(temp_dict['pic_url'])


def login1(requset):
    if requset.method == 'POST':
        # import ipdb; ipdb.set_trace()
        try:
            session_key = requset.POST.get('session_key')
            session = __read_session(session_key)
            data = {}
            # 注意验证码区分大小写
            if requset.POST['iden_code'] != session['iden_code']:
                status = 4
                data['error'] = 'verification code error'
            else:
                sql_select = 'select user_name,user_password from user_info where user_name = "' + requset.POST[
                    'user_name'] + '" and user_password = "' + requset.POST['password'] + '"'
                result_row = sql_execute(sql_select)
                status = 0
                if len(result_row):
                    data['message'] = 'login successfully'
                else:
                    data['message'] = 'login failure'
        except Exception as e:
            status = 2
            data = {'error': e}
        return JsonResponse({'status': status, 'value': data})
    elif requset.method == 'GET':
        return JsonResponse({'status': 1, 'value': {'error': 'only post allow'}})
    else:
        return JsonResponse({'status': 3, 'value': {'error': 'invalid post'}})


def login2(requset):
    if requset.method == 'POST':
        session_key = requset.POST.get('session_key', 'null')
        __read_session(session_key)
        return JsonResponse({'status': 0, 'value': {'session_key': 'success'}})
    elif requset.method == 'GET':
        return JsonResponse({'status': 1, 'value': {'error': 'only post allow'}})
    else:
        return JsonResponse({'status': 3, 'value': {'error': 'invalid post'}})
