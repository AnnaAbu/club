from django.http import JsonResponse
from .basicfunction import *
from ..utils import *
from django.shortcuts import render


def add_news(request):
    """
    添加新的文章
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
            'association_id': 'association_id',
            'activity_id': 'activity_id',
            'author_id': 'author_id',
            'article_title': 'article_title',
            # 'article_application_state': 'article_application_state',
            'article_storage': 'article_storage',
        }
        insert_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                insert_data_dict[name_change_dict[key]] = value
        insert_data_dict['article_application_state'] = '文章提交审核'
        affect_row = insert_data('article_info', insert_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def get_news_list(request):
    """
    获得文章列表 ，可以根据社团id筛选，默认显示15条，区分管理员（包括社团管理员与社联管理员）与用户两种情况
    前端的POST信息需要包含{'select_person':'',#必须
                          'select_club_id':'',#可选
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
            select_item_list = ['id', 'association_id', 'activity_id', 'author_id', 'article_title',
                                'article_application_state', 'article_storage']
            select_lim_dict = {}
        elif get_data_dict['select_person'] == 'user':
            select_item_list = ['id', 'association_id', 'activity_id', 'author_id', 'article_title',
                                'article_application_state', 'article_storage']
            select_lim_dict = {'article_application_state': '审核通过'}
        if 'select_club_id' in get_data_dict.keys():
            select_lim_dict['association_id'] = get_data_dict['select_club_id']
        get_lim_num = 15
        if 'select_lim_num' in get_data_dict.keys():
            get_lim_num = get_data_dict['select_lim_num']
        select_res_list = get_list('article_info', get_lim_num, select_item_list, select_lim_dict)
        #  将社团id转化成名字
        for item in select_res_list:
            for key in item.keys():
                if key == 'association_id':
                    res_dict = get_detail('association_info', item['association_id'], ['association_name'])
                    item['association_id'] = res_dict['association_name']
                elif key == 'activity_id':
                    res_dict = get_detail('activity_info', item['activity_id'], ['activity_name'])
                    item['activity_id'] = res_dict['activity_name']
                elif key == 'user_id':
                    res_dict = get_detail('user_info', item['user_id'], ['user_name'])
                    item['user_id'] = res_dict['user_name']
        data = {'status': 0, 'value': select_res_list}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
    return JsonResponse(data)
    # return render(request,r'login_practice.html')


def get_article_detail(request):
    """
    根据id获取article详情 GET POST均可
    :param request:
    :return:
    """
    try:
        select_article_id = 0
        if request.method == "GET":
            select_article_id = request.GET.get('select_article_id', 0)
        elif request.method == "POST":
            select_article_id = request.POST.get('select_article_id', 0)
        select_item_list = ['id', 'association_id', 'activity_id', 'author_id', 'article_title',
                            'article_application_state', 'article_storage']
        select_res_dict = get_detail('article_info', select_article_id, select_item_list)
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
            'association_id': 'association_id',
            'activity_id': 'activity_id',
            'author_id': 'author_id',
            'article_title': 'article_title',
            'article_application_state': 'article_application_state',
            'article_storage': 'article_storage',
        }
        update_data_dict = {}
        for key, value in get_data_dict.items():
            if key in name_change_dict.keys():
                update_data_dict[name_change_dict[key]] = value
        affect_row = update_data('article_info', get_data_dict['update_article_id'], update_data_dict)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)


def delete_article_info(request):
    """
    删除文章信息 需要id GET POST 均可
    :param request:
    :return:
    """
    try:
        delete_article_id = 0
        if request.method == "GET":
            delete_article_id = request.GET.get('select_article_id', 0)
        elif request.method == "POST":
            delete_article_id = request.POST.get('select_article_id', 0)
        affect_row = delete_data('article_info', delete_article_id)
        if affect_row == 1:
            data = {'status': 0}
        else:
            data = {'status': 3, 'error': 'have a wrong affect row %d' % affect_row}
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'status': 1, 'error': str(e)}
        return JsonResponse(data)
