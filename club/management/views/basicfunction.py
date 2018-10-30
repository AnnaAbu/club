from ..utils import *


def get_list(table_name, list_num, select_item_list, list_lim_dict):
    """
    获得列表形式的信息
    :param table_name: 查询表名
    :param list_num: 查询数量
    :param select_item_list: 查询字段列表
    :param list_lim_dict: 查询限制条件字典（e.g.where key = value）
    :return: 查询到的信息的以字段名为key值为value包装的字典的列表
    """
    data_dict_list = op_select(select_item_list, list_lim_dict.keys(), list_num, list_lim_dict, table_name)
    return data_dict_list


def get_detail(table_name, select_item_id, select_item_list):
    """
    获得单条形式信息，要求必须有id值
    :param table_name: 查询表名
    :param select_item_id: 查询id 详细信息查询必须依据id
    :param select_item_list: 查询字段列表
    :return: 查询到的信息的以字段名为key值为value包装的字典
    """
    sql_select = get_select_sql(select_item_list, table_name)
    sql_select += ' where id = ' + str(select_item_id)
    result_tuple = sql_execute(sql_select)
    data_dict = {}
    row = result_tuple[0]
    for i in range(len(row)):
        data_dict[select_item_list[i]] = row[i]
    return data_dict


def insert_data(table_name, insert_item_dict):
    """
    插入数据
    :param table_name: 要插入数据的表名
    :param insert_item_dict: 插入数据的字典，除了自增主键以外都需要
    :return: 影响行数，做操作执行结果判断
    """
    sql_insert = get_insert_sql(insert_item_dict, table_name)
    affect_row = sql_execute(sql_insert, affect_row=True)
    return affect_row


def update_data(table_name, update_item_dict, update_record_id):
    """
    修改数据，必须要id
    :param table_name: 要修改数据的表名
    :param update_item_dict: 要修改的字段的数据的字典
    :param update_record_id: 要修改的记录的id
    :return: 影响行数
    """
    sql_update = get_update_sql(update_record_id, update_item_dict, table_name)
    affect_row = sql_execute(sql_update, affect_row=True)
    return affect_row


def delete_data(table_name, delete_item_id):
    """
    删除数据功能（p.s.我觉得用不到）
    :param table_name: 要删除数据的表名
    :param delete_item_id: 要删除数据的id
    :return: 影响行数
    """
    sql_delete = get_delete_sql(delete_item_id, table_name)
    affect_row = sql_execute(sql_delete, affect_row=True)
    return affect_row
