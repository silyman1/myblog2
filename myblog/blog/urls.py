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
	url(r'^article/(?P<article_id>[0-9]+)/collect/$', views.collect, name='collect'),
	url(r'^article/(?P<article_id>[0-9]+)/no_collect/$', views.no_collect, name='no_collect'),
	url(r'^article/(?P<article_id>[0-9]+)/heart/$', views.heart, name='heart'),
	url(r'^article/(?P<article_id>[0-9]+)/unheart/$', views.unheart, name='unheart'),
	url(r'^author/(?P<user_id>[0-9]+)/collections/$', views.collections, name='collections'),
	url(r'^author/(?P<user_id>[0-9]+)/hearts/$', views.hearts, name='hearts'),
	url(r'^author/(?P<user_id>[0-9]+)/following/$', views.myfollowing, name='myfollowing'),
	url(r'^author/(?P<user_id>[0-9]+)/followers/$', views.myfollowers, name='myfollowers'),
	url(r'^article/(?P<article_id>[0-9]+)/detail/$', views.post_detail, name='post_detail'),
	url(r'^article/(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment'),
	url(r'^article/(?P<article_id>[0-9]+)/delete$', views.delete, name='delete'),
	url(r'^comment/(?P<comment_id>[0-9]+)/delete$', views.delete_comment, name='delete_comment'),
	url(r'^send_message/(?P<article_id>[0-9]+)/$', views.send_message, name='send_message'),
	url(r'^author/(?P<user_id>[0-9]+)/messages/$', views.messages, name='messages'),
	url(r'^message/(?P<message_id>[0-9]+)/detail/$', views.message_detail, name='message_detail'),
	url(r'^message/(?P<message_id>[0-9]+)/readed/$', views.message_read, name='message_read'),
    #url(r'^login/$', views.login_view name='login') ,
    #url(r'^logout/$', views.logout_view name='logout'),
]