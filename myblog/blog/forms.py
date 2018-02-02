#--coding=utf-8
from django import forms
class LoginForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=50)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())
class PostForm(forms.Form):
	body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'在此填入你想要写的内容：','cols':'100','rows':'40'}))
	TYPE_LIST =[
	(0,'旅行'),
	(1,'美食'),
	(2,'读书'),
	(3,'电影'),
	(4,'杂记'),
	]
	type = forms.IntegerField(widget=forms.Select(choices=TYPE_LIST,attrs={'name':"demo-category","id":"demo-category"}))