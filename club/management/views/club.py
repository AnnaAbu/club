from django.shortcuts import render


def index(request):
    return render(request, 'index_practice.html')


def activityform_practice(request):
    return render(request, 'activityform_practice.html')


def activity_list(request):
    return render(request, 'activity_list.html')


def activity_practice(request):
    return render(request, 'activity_practice.html')


def admin_add(request):
    return render(request, 'admin-add.html')


def admin_list(request):
    return render(request, 'admin-list.html')


def article_add(request):
    return render(request, 'article-add.html')


def article_list(request):
    return render(request, 'article-list.html')


def article_detail(request):
    return render(request, 'article_detail.html')


def back_practice(request):
    return render(request, 'back_practice.html')


def backmain_practice(request):
    return render(request, 'backmain_practice.html')


def communtityform_practice(request):
    return render(request, 'communtityform_practice.html')


def getin_form(request):
    return render(request, 'getin_form.html')


def login_practice(request):
    return render(request, 'login_practice.html')


from django.http import JsonResponse
from .basicfunction import *
from ..utils import *
from django.shortcuts import render


def add_club(request):
    """
    添加社团，具体字段见name_change_dict
    :param request:
    :return:
    """
    try:
        get_data_dict = {}
        if request.method == "GET":
            data = {'status': 2, 'error': 'Wrong request method'}
            return JsonResponse(data)
        elif request.method == "POST":
            get_data_dict = request.POST
        name_change_dict = {
            'association_name': 'association_name',
            'association_telephone': 'association_telephone',
            'association_teacher': 'association_teacher',
            'association_type': 'association_type',
            'association_state': 'association_state',
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['user_state'] = "等待审核"
        affect_row = insert_data('user_info', insert_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def get_user_list(request):
    """
    获取社团列表 可根据社团id查询
    前端的POST信息需要包含{ 'select_club_type':'',#可选
                          'select_lim_num':'',#可选
                          }
    :param request:{method:POST}
    :return:
    """
    try:
        # import ipdb;ipdb.set_trace()
        get_data_dict = {}
        if request.method == "GET":
            data = {'status': 2, 'error': 'Wrong request method'}
            return JsonResponse(data)
        elif request.method == "POST":
            get_data_dict = request.POST
        select_item_list = []
        select_lim_dict = {}
        select_item_list = ["id", "association_name", "association_telephone", "association_teacher",
                            "association_type", "association_state"]
        if 'select_club_type' in get_data_dict.keys():
            select_lim_dict['association_type'] = get_data_dict['select_club_type']
        get_lim_num = 15
        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num = get_data_dict['select_lim_num']
        select_res_list = get_list('association_info', get_lim_num, select_item_list, select_lim_dict)
        data = {'status': 0, 'value': select_res_list}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
    return JsonResponse(data)


def get_user_detail(request):
    """
    根据id获取user详情 GET POST均可
    :param request:
    :return:
    """
    try:
        select_user_id = 0
        if request.method == "GET":
            select_activity_id = request.GET.get('select_activity_id', 0)
        elif request.method == "POST":
            select_activity_id = request.POST.get('select_activity_id', 0)
        select_item_list = ["id", "association_name", "association_telephone", "association_teacher",
                            "association_type", "association_state"]
        select_res_dict = get_detail('association_info', select_user_id, select_item_list)
        data = {'status': 0, 'value': select_res_dict}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def update_user(request):
    """
    根据id与修改数据字典修改数据库中记录 必须POST 必须有update_association_id
    :param request:
    :return:
    """
    try:
        get_data_dict = {}
        if request.method == "GET":
            data = {'status': 2, 'error': 'Wrong request method'}
            return JsonResponse(data)
        elif request.method == "POST":
            get_data_dict = request.POST
        name_change_dict = {
            'association_name': 'association_name',
            'association_telephone': 'association_telephone',
            'association_teacher': 'association_teacher',
            'association_type': 'association_type',
            'association_state': 'association_state',
        }
        update_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                update_data_dict[name_change_dict[key]] = value
        affect_row = update_data('association_info', get_data_dict['update_association_id'], update_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)
