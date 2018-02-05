#--coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm,PostForm
from .models import User,Post
# Create your views here.
@csrf_exempt
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		email  = request.POST['email']
		password2 = request.POST['password-repeat']
		user=User.objects.create_user(username=username,password=password,email=email)
		print "register",user
		if user:
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect(reverse('blog:index'))
		else:
			return HttpResponse("注册失败")

	else:
		return render_to_response('regist.html')
@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		for key in request.POST:
			print key
		'''
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			username =loginform.cleaned_data['username']
			password =loginform.cleaned_data['password']
		'''
		username =request.POST['uname']
		password =request.POST['psw']
		user = authenticate(username=username,password=password)
		print 'user:',user
		if user:
			login(request,user)
			return redirect(reverse('blog:index'))
		return render_to_response('login.html')
	else:
		return render_to_response('login.html')
def logout_view(request):
	logout(request)
	return redirect(reverse('blog:index'))
@csrf_exempt
def index(request):
	print request.user.is_authenticated()
	#article_list = get_object_or_404
	article_list = Post.objects.order_by('-time_to_post')
	#return render_to_response("index.html",{"article_list":article_list})
	return render(request,'index.html',{"article_list":article_list})
def home(request,user_id):
	return HttpResponse("hello")
def travel(request):
	return HttpResponse("hello")

def foods(request):
	return HttpResponse("hello")
def movies(request):
	return HttpResponse("hello")
def reading(request):
	return HttpResponse("hello")
def notes(request):
	return HttpResponse("hello")
def home(request):
	return HttpResponse("hello")
@csrf_exempt
def blog_post(request,user_id):
	if request.method == 'POST':
		print '*****************'
		for key in request.POST:
			print key
		postform =PostForm(request.POST)
		if postform.is_valid():
			post = Post()
			try:
				file = request.FILES['picfile']
				pass
			except:
				pass
			post.body =postform.cleaned_data['body']
			post.type =postform.cleaned_data['type']
			post.save()
			print u'发表成功'
		return redirect(reverse('blog:index'))
	else:
		print '*****************'
		postform =PostForm()
		return render(request,'write_post.html',{"postform":postform})
def submit_post(request):
	pass