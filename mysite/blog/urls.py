from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^regist/$', views.regist),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^article/$', views.article),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),

]