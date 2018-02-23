#--coding=utf-8
from django.db import models
#扩展django自带user
from django.contrib.auth.models import AbstractUser
from django.db.models import Count
# Create your models here.

class User(AbstractUser,models.Model):
	user_register_time = models.DateTimeField('date to register',auto_now_add=True)
	mysignature = models.TextField(null=True)
	last_seen = models.DateTimeField(auto_now=False, auto_now_add=True)
	avatar = models.CharField(max_length=200,default='avatar-default.jpg')
	def get_followers(self):
	#关注的人
		user_list=[]
		for follower_ship in self.followed.all():
			user_list.append(follower_ship.follower)
		return user_list
	def get_followed(self):
	#关注我的人
		user_list=[]
		a = self.follower.all().aggregate(Count("id"))
		print a.get('id__count'),'testhere222'
		for followed_ship in self.follower.all():
			user_list.append(followed_ship.followed)
		return user_list
	def __unicode__(self):
		return self.username#返回unicode
class Post(models.Model):
	body = models.TextField(null=True)
	title = models.CharField(max_length=100,default="")
	brief = models.CharField(max_length=100,default="")
	type = models.CharField(max_length=100)
	post_image = models.CharField(max_length=200,null=True)
	post_time = models.DateTimeField('time_to_post',auto_now_add=True)
	author = models.ForeignKey(User,related_name="author")
	collection = models.ManyToManyField(User,related_name="collector")
	heart = models.ManyToManyField(User,related_name="heart_man")
	heart_num = models.PositiveIntegerField(default = 0)
	img_num = models.PositiveIntegerField(default = 0)
	comment_num = models.PositiveIntegerField(default = 0)
	collection_num = models.PositiveIntegerField(default = 0)
	def __unicode__(self):
		return self.title#返回unicode
class Picture(models.Model):
	image_url = models.CharField(max_length=200)
	article = models.ForeignKey(Post)
	type = models.CharField(max_length=100,default="1")
	

class Friendship(models.Model):
	followed = models.ForeignKey(User,related_name="followed")
	follower = models.ForeignKey(User,related_name="follower")

class Comment(models.Model):
	commentor = models.ForeignKey(User,on_delete=models.CASCADE)
	article = models.ForeignKey(Post,on_delete=models.CASCADE)
	content = models.CharField(max_length=100,default="")
	timestamp = models.DateTimeField('time_to_comment',auto_now=True)