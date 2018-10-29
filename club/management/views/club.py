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
