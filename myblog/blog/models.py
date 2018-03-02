#--coding=utf-8
from django.db import models
#扩展django自带user
from django.contrib.auth.models import AbstractUser
from django.db.models import Count
from django.db.models.signals import post_save,post_delete
from django.contrib.contenttypes.models import ContentType  
from django.contrib.contenttypes import generic
# Create your models here.04

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
	#events = generic.GenericRelation('Event') 
	def __unicode__(self):
		return self.title#返回unicode
	def description(self):  
		return u'%s 发表了博客《%s》' % (self.author, self.title)  
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
	timestamp = models.DateTimeField('time_to_comment',auto_now_add=True)
class Message(models.Model):
	#user_id = models.IntegerField(db_index=True)
	has_readed = models.BooleanField(default=False)
	content = models.CharField(max_length=100,null=True)
	sender = models.ForeignKey(User,related_name="sender")
	receiver = models.ManyToManyField(User,related_name="receiver")
	timestamp = models.DateTimeField('time_to_send',auto_now_add=True)
	post_id = models.IntegerField(null=True)
	
class UserMessagesCount(models.Model):
	user_id = models.IntegerField(primary_key=True)
	unread_count = models.IntegerField(default=0)
	total_count = models.IntegerField(default=0)
	
	def __str__(self):
		return '<UserMessagesCount %s: %s>' % (self.user_id, self.unread_count)

'''
class Event(models.Model):  
	user = models.ForeignKey(User)  
	content_type = models.ForeignKey(ContentType)  
	object_id = models.PositiveIntegerField()  
      
	event = generic.GenericForeignKey('content_type', 'object_id')  
      
	created = models.DateTimeField(u'事件发生时间', auto_now_add = True)  
      
	def __unicode__(self):  
		return self.user.username + u'的新鲜事'  
	def description(self):  
		return self.event.description()  
def post_post_save(sender, instance, signal, *args, **kwargs):  
	post = instance   
	event = Event(user=post.author,event = post)  
	event.save()

dispatcher.connect(post_post_save, signal=signals.post_save, sender=Post)  
class UserMessagesCount(models.Model):
	user_id = models.IntegerField(primary_key=True)
	unread_count = models.IntegerField(default=0)
	
	def __str__(self):
		return '<UserMessagesCount %s: %s>' % (self.user_id, self.unread_count)
'''