#--coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^travel/$', views.travel, name='travel'),
	url(r'^foods/$', views.foods, name='foods'),
	url(r'^movies/$', views.movies, name='movies'),
	url(r'^reading/$', views.reading, name='reading'),
	url(r'^notes/$', views.notes, name='notes'),
	url(r'^author/(?P<user_id>[0-9]+)/home/$', views.home, name='home'),
	url(r'^register/$', views.register, name='register'),
	url(r'^author/(?P<user_id>[0-9]+)/write_blog/$', views.blog_post, name='blog_post'),
	url(r'^author/(?P<user_id>[0-9]+)/information/$', views.get_information, name='get_information'),
	url(r'^author/(?P<user_id>[0-9]+)/edit/$', views.edit, name='edit'),
	url(r'^author/(?P<user_id>[0-9]+)/follow/$', views.follow, name='follow'),
	url(r'^author/(?P<user_id>[0-9]+)/unfollow/$', views.unfollow, name='unfollow'),
    #url(r'^login/$', views.login_view name='login') ,
    #url(r'^logout/$', views.logout_view name='logout'),
]