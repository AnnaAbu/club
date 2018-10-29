from django.http import JsonResponse
from ..utils import *
from .basicfunction import *
from django.shortcuts import render




def add_finance(request):
    """
    添加新的财务预算申请

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
            'finance_amount': 'finance_amount',
            'association_id': 'association_id',
            'activity_id': 'activity_id',
            'finance_application_state': 'finance_application_state',
            'finance_storage': 'finance_storage'
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['finance_application_state'] = '财务预算已提交'
        affect_row = insert_data('finance_info',insert_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)

def get_finance_list(request):
    """
    根据id查找财务申请列表,区分管理员与普通用户，若无id则显示前15条或指定条数
    前端的POST信息需要包含{'select_person':'',#必须
                          'select_club_id':'',#可选
                          'select_lim_num':'',#可选
                          }
    :param request:
    :return:
    """

    try:
        get_data_dict={}
        if request.method=="GET":
            data={'status':2,"error":'Wrong request method'}
            return JsonResponse(data)
        elif request.method=="POST":
            get_data_dict=request.POST

        select_item_list=[]
        select_lim_dict={}

        if get_data_dict['select_person'] == "admin":
            select_item_list = ['finance_amount', 'association_id', 'activity_id',
                                'finance_application_state', 'finance_storage']
            select_lim_dict={}
        elif get_data_dict['select_person'] == "user":
            select_item_list = ['finance_amount', 'association_id', 'activity_id',
                                'finance_application_state']
            select_lim_dict={'finance_application_state':'审核通过'}
            ##是否需要区分提交的用户和其他的用户？

        if 'select_club_id' in get_data_dict.keys():
            select_lim_dict['association_id']=get_data_dict['select_club_id']

        ##是否需要使用活动id检索？
        get_lim_num = 15
        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num=get_data_dict['select_lim_num']
        select_res_list=get_list('finance_info',get_lim_num,select_item_list,select_lim_dict)
        data={'status':0,'value':select_res_list}

        return JsonResponse(data)

    except Exception as e:
        print(e)
        data={'status':1,'error':str(e)}
    return JsonResponse(data)


def get_finance_detail(request):
    """
    查找某个具体的财务申请,必须提交id

    :param request:
    :return:
    """
    try:
        select_finance_id = 0
        if request.method == "GET":
            select_finance_id = request.GET.get('select_finance_id', 0)
        elif request.method == "POST":
            select_finance_id = request.POST.get('select_finance_id', 0)
        select_item_list = ['finance_amount', 'association_id', 'activity_id',
                            'finance_application_state', 'finance_storage']
        select_res_dict = get_detail('finance_info', select_finance_id, select_item_list)
        data = {'status': 0, 'value': select_res_dict}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def update_finance(request):
    """
    更新财务申请的状态

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
            'finance_amount': 'finance_amount',
            'association_id': 'association_id',
            'activity_id': 'activity_id',
            'finance_application_state': 'finance_application_state',
            'finance_storage': 'finance_storage'
        }
        update_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                update_data_dict[name_change_dict[key]] = value
        affect_row = update_data('finance_info', get_data_dict['update_finance_id'], update_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)
