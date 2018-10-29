from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def login(request):
    """

    :param request: {method:post,header: * ,request.POST.get():{user_id:int,psw:string(MD5),verif_code:string}}
    data = {login_status: boolean,cookie: string }
    :return:JsonResponse(data)
    """
    data = 0
    return JsonResponse(data)


def get_verification_code(request):
    """

    :param request:{method:get}
    data = {pic_location:string,cookie:string}
    :return: JsonResponse(data)
    """
    # make_verification_code()
    cookie = ""
    pic_location = ""  # 图片存储位置
    data = {"pic_location": pic_location, "cookie": cookie}
    return JsonResponse(data)


def get_club_list(request):
    """

    :param request:{method:post}
    request.POST.get():{club_category:string}

    data = {status:int,value:[{club_id:int,club_name:string},{}]}
    :return: JsonResponse(data)
    """
    data = {}
    return JsonResponse(data)


def get_news_list(request):
    """

    :param request: {method:post}
    request.POST.get():{club_category:string,club_name:string,KMP_string:string,news_num:int}
    data = {status:int,value:[{news_id:int,new_title:string,news_time:datetime(string)},{}]}
    :return: JsonResponse(data)
    """
    data = {}
    return JsonResponse(data)

def get_activity_list(request):
    """

    :param request:
    :return:
    """
    data = {}
    return JsonResponse(data)

def get_club_detail(request):
    """

    :param request:{method,get}
    request.GET.get():{club_id:int}
    data = {status:int,value:{key:value for key in table_name_list for value in select_res_list}}
    :return: data
    """
    data = {}
    return JsonResponse(data)


def get_news_detail(request):
    """

    :param request:{method,get}
    request.GET.get():{news_id:int}
    data = {status:int,value:{key:value for key in table_name_list for value in select_res_list}}
    :return: data
    """
    data = {}
    return JsonResponse(data)


def add_news(request):
    """

    :param request: {method:post}
    request.POST.get():{} ##news的表单内容
    data = {status:int}
    :return: JsonResponse(data)
    """
    data = {}
    return JsonResponse(data)

##其他添加类似 e.g.新社团 活动 财务 主要为post给参数 insert数据库 返回状态（以及id？ ）

def add_club(request):
    """

    :param request:{method:post}

    :return:
    """
    pass

def add_activity(request):
    """

    :param request:{method:post}
    :return:
    """
    pass

def audit(request):
    """

    :param request:
    :return:
    """
    pass