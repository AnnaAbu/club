from django.http import JsonResponse
from .basicfunction import *
from ..utils import *
from django.shortcuts import render


def add_activity(request):
    """
    添加新的社团活动
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
            'activity_name': 'activity_name',
            'start_time': 'activity_start_time',
            'stop_time': 'activity_end_time',
            'fz_telephone': 'activity_telephone',
            'space': 'activity_place',
            # '??':'activity_person',#待增加前端表单
            # '?':'activity_ association' #待增加前端表单
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['activity_state'] = '社团提交申请'
        affect_row = insert_data('activity_info', insert_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def get_activity_list(request):
    """
    获得社团活动列表 ，可以根据社团id筛选，默认显示15条，区分管理员（包括社团管理员与社联管理员）与用户两种情况
    前端的POST信息需要包含{'select_person':'',#必须
                          'select_club_id':'',#可选
                          'select_lim_num':'',#可选
                          }
    :param request:
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
        if get_data_dict['select_person'] == 'admin':
            select_item_list = ['id', 'activity_name', 'activity_person', 'activity_telephone', 'activity_start_time',
                                'activity_end_time', 'activity_place', 'activity_association', 'activity_state']
            select_lim_dict = {}
        elif get_data_dict['select_person'] == 'user':
            select_item_list = ['id', 'activity_name', 'activity_start_time', 'activity_end_time', 'activity_place',
                                'activity_association']
            select_lim_dict = {'activity_state': '审核通过'}
        if 'select_club_id' in get_data_dict.keys():
            select_lim_dict['activity_association'] = get_data_dict['select_club_id']
        get_lim_num = 15
        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num = get_data_dict['select_lim_num']
        select_res_list = get_list('activity_info', get_lim_num, select_item_list, select_lim_dict)
        #  将社团id转化成名字
        for item in select_res_list:
            for key in item.keys():
                if key == 'activity_association':
                    res_dict = get_detail('association_info', item['activity_association'], ['association_name'])
                    item['activity_association'] = res_dict['association_name']
        data = {'status': 0, 'value': select_res_list}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
    return JsonResponse(data)
    # return render(request,r'login_practice.html')


def get_activity_detail(request):
    """
    根据id获取activity详情 GET POST均可
    :param request:
    :return:
    """
    try:
        select_activity_id = 0
        if request.method == "GET":
            select_activity_id = request.GET.get('select_activity_id', 0)
        elif request.method == "POST":
            select_activity_id = request.POST.get('select_activity_id', 0)
        select_item_list = ['activity_name', 'activity_person', 'activity_telephone', 'activity_start_time',
                            'activity_end_time', 'activity_place', 'activity_association', 'activity_state']
        select_res_dict = get_detail('activity_info', select_activity_id, select_item_list)
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


def update_activity_info(request):
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
            'activity_name': 'activity_name',
            'start_time': 'activity_start_time',
            'stop_time': 'activity_end_time',
            'fz_telephone': 'activity_telephone',
            'space': 'activity_place',
            # '??':'activity_person',#待增加前端表单
            # '?':'activity_ association' #待增加前端表单
            'activity_state': 'activity_state'  # 不知道前端如何命名该字段
        }
        update_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                update_data_dict[name_change_dict[key]] = value
        affect_row = update_data('activity_info', get_data_dict['update_activity_id'], update_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def delete_activity_info(request):
    """
    删除活动信息 需要id GET POST 均可
    :param request:
    :return:
    """
    try:
        delete_activity_id = 0
        if request.method == "GET":
            delete_activity_id = request.GET.get('select_activity_id', 0)
        elif request.method == "POST":
            delete_activity_id = request.POST.get('select_activity_id', 0)
        affect_row = delete_data('activity_info', delete_activity_id)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


# 以下关于活动报名的功能没有在urls中进行配置，使用前请配置urls

def add_activity_application(request):
    """
    添加报名申请，必须需要学工号、活动id、提交申请时间，注意时间格式 猜想可能出现数据库相关错误，但处理难度应该不大
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
            'activity_id': 'activity_id',
            'application_time': 'application_time',
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['application_state'] = '用户提交报名信息'
        affect_row = insert_data('activity_application_info', insert_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def get_activity_application(request):
    """
    获得活动报名信息列表 ，可以根据活动id筛选，默认显示15条，区分管理员（包括社团管理员与社联管理员）与用户两种情况
    前端的POST信息需要包含{'select_person':'',#必须
                          'select_activity_id':'',#可选
                          'select_lim_num':'',#可选
                          }
    :param request:
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
        if get_data_dict['select_person'] == 'admin':
            select_item_list = ['id', 'user_id', 'activity_id', 'application_time', 'application_state']
            select_lim_dict = {}
        elif get_data_dict['select_person'] == 'user':
            select_item_list = ['id', 'user_id', 'activity_id', 'application_time', 'application_state']
            select_lim_dict = {'activity_state': '审核通过'}
        if 'select_activity_id' in get_data_dict.keys():
            select_lim_dict['activity_id'] = get_data_dict['select_activity_id']
        get_lim_num = 15
        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num = get_data_dict['select_lim_num']
        select_res_list = get_list('activity_info', get_lim_num, select_item_list, select_lim_dict)
        #  将社团id转化成名字
        for item in select_res_list:
            for key in item.keys():
                if key == 'activity_id':
                    res_dict = get_detail('activity_info', item['activity_id'], ['activity_name'])
                    item['activity_id'] = res_dict['activity_name']
        data = {'status': 0, 'value': select_res_list}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
    return JsonResponse(data)


def update_activity_application(request):
    """
    根据id与修改数据字典修改数据库中记录 必须POST 必须有update_activity_application_id
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
            'activity_id': 'activity_id',
            'application_time': 'application_time',
            'application_state': 'application_state'
        }
        update_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                update_data_dict[name_change_dict[key]] = value
        affect_row = update_data('activity_application_info', get_data_dict['update_application_activity_id'],
                                 update_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)
