#--coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm,PostForm,EditForm
from .models import User,Post,Picture,Friendship
from PIL import Image
from django.utils import timezone
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
			user.last_seen = timezone.now()
			user.save()
			print user.last_seen
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
	article_list = Post.objects.order_by('-post_time')
	img_list = Picture.objects.all()
	print "img",img_list
	print 'aa'
	for article in article_list:
		for img in img_list:
			print img.article
			if img.article.title==article.title:
				print img.image_url
				print "right"
		print article.title
	#return render_to_response("index.html",{"article_list":article_list})
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list})
def travel(request):
	article_list = Post.objects.filter(type=0).order_by('-post_time')
	img_list = Picture.objects.filter(type=0)
	for article in article_list:
		print article.title
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list})

def foods(request):
	article_list = Post.objects.filter(type=1).order_by('-post_time')
	img_list = Picture.objects.filter(type=1)
	for article in article_list:
		print article.title
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list})
def movies(request):
	article_list = Post.objects.filter(type=3).order_by('-post_time')
	img_list = Picture.objects.filter(type=3)
	for article in article_list:
		print article.title
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list})
def reading(request):
	article_list = Post.objects.filter(type=2).order_by('-post_time')
	img_list = Picture.objects.filter(type=2)
	for article in article_list:
		print article.title
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list})
def notes(request):
	article_list = Post.objects.filter(type=4).order_by('-post_time')
	img_list = Picture.objects.filter(type=4)
	for article in article_list:
		print article.title,article.author.id
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list})
def home(request,user_id):
	article_list = request.user.post_set.all().order_by('-post_time')
	img_list = Picture.objects.all()
	print article_list
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list})
@csrf_exempt
def blog_post(request,user_id):
	if request.method == 'POST':
		print '*****************'
		for key in request.POST:
			print key
		postform =PostForm(request.POST)
		if postform.is_valid():
			post = Post()
			post.body =postform.cleaned_data['body']
			post.type =postform.cleaned_data['type']
			post.title =postform.cleaned_data['title']
			post.brief =postform.cleaned_data['brief']
			post.author = request.user
			post.save()
			try:
				#file_list = request.POST.getlist('picfile')
				file_list = request.FILES.getlist('picfile')
				print file_list
				i =0
				for file in file_list:
					pic = Picture()
					i +=1
					print file.name
					img = Image.open(file)
					img.thumbnail((500,500),Image.ANTIALIAS)
					name = post.title + str(i)
					for type in ['gif','jpeg','jpg','png','JPG']:
						if file.name.endswith(type):
							img.save("E:\\gitprojects\\myblog2\\myblog\\blog\\static\\images\\%s.%s"%(name,type))
							break
						else:
							print 'nonono'
					#product.image_url = name+'.gif'
					pic.image_url= "%s.%s"%(name,type)
					print "1"
					pic.type = post.type
					print "2"
					pic.article=post
					print "3"
					pic.save()
					print "4"
			except Exception,e:
				return HttpResponse("Error %s"%e)#异常，查看报错信息
			print u'发表成功'
		return redirect(reverse('blog:index'))
	else:
		print '*****************'
		postform =PostForm()
		return render(request,'write_post.html',{"postform":postform})
def get_information(request,user_id):
	user = get_object_or_404(User,pk= user_id)
	article_list = Post.objects.filter(author=user).order_by('-post_time')
	img_list = Picture.objects.all()
	title = user.username + u"的个人信息主页"
	followers_list= user.get_followers()
	print request.user
	print followers_list
	followed_list = user.get_followed()
	print followed_list
	return render(request,'information.html',{"user":user,
											"article_list":article_list,
											"img_list":img_list,
											"title":title,
											"followers_list":followers_list,
											"followed_list":followed_list,
											"followers_length":len(followers_list),
											"followed_length":len(followed_list)})
@csrf_exempt
def edit(request,user_id):
	if request.method == 'POST':
		editform =EditForm(request.POST)
		if editform.is_valid():
			request.user.username =editform.cleaned_data['username']
			request.user.email =editform.cleaned_data['email']
			request.user.mysignature =editform.cleaned_data['mysignature']
			request.user.save()
			print u'修改成功'
		else:
			print editform.errors
			print u'w无效'
		return redirect(reverse('blog:get_information',args=(request.user.id,)))
	else:
		data = {'username':request.user.username,'email':request.user.email,'mysignature':request.user.mysignature}
		editform =EditForm(initial =data)
		return render(request,'edit.html',{"editform":editform})
def follow(request,user_id):
	flag = set_follower(request.user,user_id)
	if flag:
		print u'关注成功'
	else:
		print u'关注shibai'
	return redirect(reverse('blog:get_information',args=(user_id,)))
def unfollow(request,user_id):
	user = get_object_or_404(User,pk= user_id)
	friendship = Friendship.objects.filter(followed =request.user,follower=user)
	friendship.delete()
	print u'取消关注成功'
	return redirect(reverse('blog:get_information',args=(user_id,)))
def set_follower(selfuser,id):
	try:
		user = User.objects.get(pk=id)
		print u'关注shibai1'
	except Exception:
		return None
	# 这是关注的逻辑
	print u'关注shibai2'
	friendship = Friendship()
	print u'关注shibai3'
	friendship.followed = selfuser
	print u'关注shibai4'
	friendship.follower = user
	print u'关注shibai5'
	friendship.save()
	print u'关注shibai6'
	return True
def submit_post(request):
	pass