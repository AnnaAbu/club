from django.http import JsonResponse
from .basicfunction import *
from ..utils import *
from django.shortcuts import render


def add_users(request):
    """
    添加用户，具体字段见name_change_dict
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
            'user_id': 'user_id',
            'user_name': 'user_name',
            'user_password': 'user_password',
            'user_identity': 'user_identity',
            'association_id': 'association_id',
            'user_sex': 'user_sex',
            'user_telephone': 'user_telephone'
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['user_status'] = 2
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


def get_users_list(request):
    """
    获取用户列表 可根据社团id查询
    前端的POST信息需要包含{ 'select_club_id':'',#可选
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
        select_item_list = ['user_id', 'user_name', 'user_identity', 'association_id', 'user_sex','user_telephone']
        if 'select_club_id' in get_data_dict.keys():
            select_lim_dict['association_id'] = get_data_dict['select_club_id']
        get_lim_num = 15
        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num = get_data_dict['select_lim_num']
        select_res_list = get_list('user_info', get_lim_num, select_item_list, select_lim_dict)
        #  将社团id转化成名字
        print(select_res_list)
        for item in select_res_list:
            for key in item.keys():
                if key == 'association_id':
                    res_dict = get_detail('association_info', item['association_id'], ['association_name'])
                    item['association_id'] = res_dict['association_name']
        data = {'status': 0, 'value': select_res_list}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
    return JsonResponse(data)



def get_users_detail(request):
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
        select_item_list = ['user_id', 'user_name', 'user_identity', 'association_id', 'user_sex','user_telephone']
        select_res_dict = get_detail('activity_info', select_user_id, select_item_list)
        for key in select_res_dict.keys():
            if key == 'activity_association':
                res_dict = get_detail('association_info', select_res_dict['activity_association'], ['association_name'])
                select_res_dict['activity_association'] = res_dict['association_name']
        data = {'status': 0, 'value': select_res_dict}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def update_user(request):
    """
    根据id与修改数据字典修改数据库中记录 必须POST 必须有update_activity_id
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
            'user_id': 'user_id',
            'user_name': 'user_name',
            'user_password': 'user_password',
            'user_identity': 'user_identity',
            'association_id': 'association_id',
            'user_sex': 'user_sex',
            'user_telephone': 'user_telephone',
            'user_status': 'user_status'
        }
        update_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                update_data_dict[name_change_dict[key]] = value
        affect_row = update_data('user_info', get_data_dict['update_user_id'], update_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)