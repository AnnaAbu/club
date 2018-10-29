from django.contrib import admin
from django.urls import path,include
from .views import activity,news,users,place,finance,club,appraisal

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path(r'club_management/', include('management.urls'))
    path(r'index/',club.index),
    path(r'activityform_practice/',club.activityform_practice),
    path(r'activity_list/',club.activity_list),
    path(r'activity_practice/',club.activity_practice),
    path(r'admin_add/',club.admin_add),
    path(r'admin_list',club.admin_list),
    path(r'article_add',club.article_add),
    path(r'article_list',club.article_list),
    path(r'article_detail',club.article_detail),
    path(r'back_practice',club.back_practice),
    path(r'backmain_practice',club.backmain_practice),
    path(r'communityform_practice',club.communtityform_practice),
    path(r'getin_form',club.getin_form),
    path(r'login_practice',club.login_practice),







    path(r'get_activity_list/',activity.get_activity_list),
    path(r'get_activity_detail/',activity.get_activity_detail),
    # path(r'delete_activity/',activity.delete_activity),
    # path(r'update_activity/',activity.update_activity),
    path(r'add_activity/',activity.add_activity),
    #
    # path(r'get_news_list/',news.get_news_list),
    # path(r'get_news_detail/',news.get_news_detail),
    # path(r'delete_news/',news.delete_news),
    # path(r'update_news/',news.update_news),
    # path(r'add_news/',news.add_news),
    #
    # path(r'get_users_list/',users.get_users_list),
    # path(r'get_users_detail/',users.get_users_detail),
    # path(r'delete_users/',users.delete_users),
    # path(r'update_users/',users.update_users),
    # path(r'add_users/',users.add_users),
    #
    # path(r'get_place_list/',place.get_place_list),
    # path(r'get_place_detail/',place.get_place_detail),
    # path(r'delete_place/',place.delete_place),
    # path(r'update_place/',place.update_place),
    # path(r'add_place/',place.add_place),
    #
    # path(r'get_finance_list/',finance.get_finance_list),
    # path(r'get_finance_detail/',finance.get_finance_detail),
    # path(r'delete_finance/',finance.delete_finance),
    # path(r'update_finance/',finance.update_finance),
    # path(r'add_finance/',finance.add_finance),
    #
    # path(r'get_club_list/', club.get_club_list),
    # path(r'get_club_detail/', club.get_club_detail),
    # path(r'delete_club/', club.delete_club),
    # path(r'update_club/',club.update_club),
    # path(r'add_club/', club.add_club),
    #
    # path(r'update_appraisal/', appraisal.update_appraisal),

]