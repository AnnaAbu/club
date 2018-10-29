from django.http import JsonResponse
from ..utils import *
from .basicfunction import *
from django.shortcuts import render




def add_activity(request):
    """

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
            #'??':'activity_person',
            #'?':'activity_ association'
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['activity_state'] = '社团提交申请'
        affect_row = insert_data('activity_info',insert_data_dict)
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

    :param request:
    :return:
    """
    # data = {}
    # return JsonResponse(data)
    return render(request,r'login_practice.html')

def get_activity_detail(request):
    """

    :param request:
    :return:
    """
    data = {}
    return JsonResponse(data)
