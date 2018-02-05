#--coding=utf-8
from django.db import models
#扩展django自带user
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser,models.Model):
	user_register_time = models.DateTimeField('date to register',auto_now_add=True)
	mysignature = models.TextField(null=True)
	last_seen = models.DateTimeField(auto_now=False, auto_now_add=True)
	def __unicode__(self):
		return self.username#返回unicode
class Post(models.Model):
	body = models.TextField(null=True)
	title = models.CharField(max_length=100,default="")
	brief = models.CharField(max_length=100,default="")
	type = models.CharField(max_length=100)
	post_image = models.CharField(max_length=200,null=True)
	post_time = models.DateTimeField('time_to_post',auto_now=False, auto_now_add=True)
	author = models.ForeignKey(User)