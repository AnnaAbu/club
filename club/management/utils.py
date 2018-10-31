# -*- coding: utf-8 -*-
from django.conf import settings
import MySQLdb

DATABASES = settings.DATABASES['default']


# 当进行插入操作时，affect_row=True查看影响行数
# 进行读取操作时，affect_row=False拿到读取结果

def sql_execute(sql, affect_row=False):
    database = MySQLdb.connect(host=DATABASES['HOST'], user=DATABASES['USER'], passwd=DATABASES['PASSWORD'],
                               db=DATABASES['NAME'], charset="utf8")
    cursor = database.cursor()
    cursor.execute(sql)
    if affect_row:
        ct = cursor.rowcount
    else:
        ct = cursor.fetchall()
    cursor.close()
    database.commit()
    database.close()
    return ct


def get_insert_sql(data_dict, table):
    sql_insert = 'insert into ' + table + '('
    sql_keys = ''
    sql_values = ''
    for key, value in data_dict.items():
        sql_keys += '`' + key + '`,'
        sql_values += '"' + str(value).replace('"', "'") + '",'
        print(sql_values)
    sql_insert = sql_insert + sql_keys[:-1] + ') values (' + sql_values[:-1] + ')'
    return sql_insert


def get_update_sql(pk_id, data_dict, table):
    sql_update = 'update ' + table + ' set '
    for key, value in data_dict.items():
        sql_update += '`' + str(key) + '` = "' + str(value).replace('"', "'") + '",'
    sql_update = sql_update[:-1]
    sql_update += ' where id =' + str(pk_id)
    return sql_update


def get_select_sql(data_list, table):
    # import ipdb;ipdb.set_trace()
    sql_select = 'select '
    for key in data_list:
        sql_select += '`' + key + '`,'
    sql_select = sql_select[:-1]
    sql_select += ' from ' + table
    return sql_select


def op_select(data_list, post_list, show_num, desc_dict, table):
    sql_select = get_select_sql(data_list, table)
    if len(post_list) != 0:
        sql_select += ' where '
        for key in post_list:
            temp_str = key + ' = ' + '"' + desc_dict[key] + '"' + ' and '
            sql_select += temp_str
        sql_select = sql_select[:-5]
    sql_select += ' order by id desc limit ' + str(show_num) + ';'
    result_tuple = sql_execute(sql_select)
    dict_list = []
    for row in result_tuple:
        temp_dict = {}
        for i in range(len(row)):
            temp_dict[data_list[i]] = row[i]
        dict_list.append(temp_dict)
    return dict_list


def get_delete_sql(del_id, table):
    sql_delete = 'delete from' + table + 'where id=' + str(del_id)
    return sql_delete
