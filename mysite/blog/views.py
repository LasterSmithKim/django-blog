# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.contrib import auth
from django import forms  # 导入表单
from django.contrib.auth.models import User  # 导入django自带的user表


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密_码', widget=forms.PasswordInput())


# Django的form的作用：
# 1、生成html标签
# 2、用来做用户提交的验证
# Form的验证思路
# 前端：form表单
# 后台：创建form类，当请求到来时，先匹配，匹配出正确和错误信息。
def index(request):
    return render(request, 'index.html')


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)  # 包含用户名和密码
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
            password = uf.cleaned_data['password']
            # 添加到数据库
            # registAdd = User.objects.get_or_create(username=username,password=password)
            registAdd = User.objects.create_user(username=username, password=password)
            # print registAdd
            if registAdd == False:
                return render(request, 'share1.html', {'registAdd': registAdd, 'username': username})

            else:
                # return HttpResponse('ok')
                return render(request, 'share1.html', {'registAdd': registAdd})
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    return render(request, 'regist1.html', {'uf': uf})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        username, password
        re = auth.authenticate(username=username, password=password)  # 用户认证
        if re is not None:  # 如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
            auth.login(request, re)  # 登陆成功
            return redirect('/', {'user': re})  # 跳转--redirect指从一个旧的url转到一个新的url
        else:  # 数据库里不存在与之对应的数据
            return render(request, 'login.html', {'login_error': '用户名或密码错误'})  # 注册失败
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def article(request):
    article_list = Article.objects.all()
    # print article_list
    # print type(article_list)
    # QuerySet是一个可遍历结构，包含一个或多个元素，每个元素都是一个Model实例
    # QuerySet类似于Python中的list，list的一些方法QuerySet也有，比如切片，遍历。
    # 每个Model都有一个默认的manager实例，名为objects，QuerySet有两种来源：通过manager的方法得到、通过QuerySet的方法得到。mananger的方法和QuerySet的方法大部分同名，同意思，如filter(),update()等，但也有些不同，如manager有create()、get_or_create()，而QuerySet有delete()等
    return render(request, 'article.html', {'article_list': article_list})


def detail(request, id):
    # print id
    try:
        article = Article.objects.get(id=id)
        # print type(article)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', locals())



