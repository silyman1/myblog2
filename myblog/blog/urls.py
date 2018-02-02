#--coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^author/(?P<user_id>[0-9]+)/write_blog/$', views.blog_post, name='blog_post'),
    #url(r'^login/$', views.login_view name='login') ,
    #url(r'^logout/$', views.logout_view name='logout'),
]