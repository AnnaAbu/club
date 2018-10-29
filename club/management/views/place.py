from django.http import JsonResponse
from .basicfunction import *
from ..utils import *
from django.shortcuts import render


def add_place_application(request):
    """
    添加新的场地申请
    :param request:{method:post}
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
            'place_id': 'place_id',
            'activity_id': 'activity_id',
            'place_application_start': 'place_application_start',
            'place_application_end': 'place_application_end',
            'place_application_state': 'place_application_state',
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['place_application_state'] = '场地申请已提交'
        affect_row = insert_data('place_application_info', insert_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def get_place_application_list(request):
    """
    获得场地申请列表,使用场地id进行检索
    前端的POST信息需要包含{'select_person':'',#必须
                          'select_place_id':'',#可选
                          'select_lim_num':'',#可选
                          }
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
        select_item_list = []
        select_lim_dict = {}
        if get_data_dict['select_person'] == 'admin':
            select_item_list = ['place_id', 'activity_id', 'place_application_start', 'place_application_end',
                                'place_application_state']
            select_lim_dict = {}
        elif get_data_dict['select_person'] == 'user':
            select_item_list = ['place_id', 'activity_id', 'place_application_start', 'place_application_end',
                                'place_application_state']
            select_lim_dict = {'place_state': '审核通过'}

        if 'select_place_id' in get_data_dict.keys():
            select_lim_dict['place_id'] = get_data_dict['select_place_id']
        get_lim_num = 15
        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num = get_data_dict['select_lim_num']
        select_res_list = get_list('place_application_info', get_lim_num, select_item_list, select_lim_dict)
        data = {'status': 0, 'value': select_res_list}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
    return JsonResponse(data)
    # return render(request,r'login_practice.html')


def get_place_application_detail(request):
    """
    根据场地申请书id获取场地申请详情
    :param request:
    :return:
    """
    try:
        select_place_application_id = 0
        if request.method == "GET":
            select_place_id = request.GET.get('select_place_application_id', 0)
        elif request.method == "POST":
            select_place_id = request.GET.get('select_place_application_id', 0)
        select_item_list = ['place_id', 'activity_id', 'place_application_start', 'place_application_end',
                            'place_application_state']
        select_res_dict = get_detail('place_application_info', select_place_application_id, select_item_list)
        data = {'status': 0, 'value': select_res_dict}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def update_place_application_info(request):
    """
    根据id与修改数据字典修改数据库中记录 必须POST 必须有update_place_id
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
            'place_id': 'place_id',
            'activity_id': 'activity_id',
            'place_application_start': 'place_application_start',
            'place_application_end': 'place_application_end',
            'place_application_state': 'place_application_state',
        }
        update_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                update_data_dict[name_change_dict[key]] = value
        affect_row = update_data('place_application_info', get_data_dict['update_place_application_id'],update_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)

def delete_place_application_info(request):
    """
    删除场地申请信息 需要id GET POST 均可
    :param request:
    :return:
    """
    try:
        delete_place_application_id = 0
        if request.method == "GET":
            delete_place_application_id = request.GET.get('select_place_application_id', 0)
        elif request.method == "POST":
            delete_place_application_id = request.POST.get('select_place_application_id', 0)
        affect_row = delete_data('place_application_info', delete_place_application_id)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)

def get_place_list(request):
    """
    获得全部场地列表
    前端的POST信息需要包含{
                          'select_lim_num':'',#可选
                          }
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

        select_item_list = ['id','place_name','place_capacity']
        select_lim_dict = {}
        get_lim_num = 15

        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num = get_data_dict['select_lim_num']
        select_res_list = get_list('place_info', get_lim_num, select_item_list, select_lim_dict)
        data = {'status': 0, 'value': select_res_list}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
    return JsonResponse(data)
    # return render(request,r'login_practice.html')


def get_place_detail(request):
    """
    根据场地id获取场地详情,我觉得没必要
    :param request:
    :return:
    """
    try:
        select_place_id = 0
        if request.method == "GET":
            select_place_id = request.GET.get('select_place_id', 0)
        elif request.method == "POST":
            select_place_id = request.GET.get('select_place_id', 0)
        select_item_list = ['place_id', 'activity_id', 'place_application_start', 'place_application_end',
                            'place_application_state']
        select_res_dict = get_detail('place_info', select_place_id, select_item_list)
        data = {'status': 0, 'value': select_res_dict}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)