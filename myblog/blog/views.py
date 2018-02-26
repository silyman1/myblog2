#--coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm,PostForm,EditForm,CommentForm,MessageForm
from .models import User,Post,Picture,Friendship,Comment,Message
from PIL import Image
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
class CustemPaginator(Paginator):
	def __init__(self, current_page, max_pager_num, *args, **kwargs):
		# 当前页
		self.current_page = int(current_page)
		# 最多显示的页码数量
		self.max_pager_num = int(max_pager_num)
		super(CustemPaginator,self).__init__(*args, **kwargs)
	def page_num_range(self):
		# 当前页
		# self.current_page
		# 最多显示的页码数量 11
		# self.per_pager_num
		# 总页数
		# self.num_pages
		# 判断如果页面总数量小于显示页面的总数量，那么返回最大的页面总数量。
		if self.num_pages < self.max_pager_num:
			return range(1, self.num_pages + 1)
		part = int(self.max_pager_num / 2)
		# 判断当前页小于等于最大显示页的一半，那么返回1到最大显示页数量。
		if self.current_page <= part:
			return range(1, self.max_pager_num + 1)
		# 当选择页数加上显示页数的一半的时候，说明越界了，例如最大也数是15，显示页数是10，我选择11页，那么11+5等于16，大于15，那么就显示总页数15-11+1，15+1
		if (self.current_page + part) > self.num_pages:
		# 那么返回总页数前去当前显示页数个数+1的值，和总页数+1的值。
			return range(self.num_pages - self.max_pager_num + 1, self.num_pages + 1)
		# 当选择页大于当前总页数的一半的时候，返回当前选择页的前五个和后五个页数。
		return range(self.current_page - part, self.current_page + part + 1)
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
	introduce_list = Post.objects.order_by('-heart_num')[:4]
	introduce_pic_list = []
	for a in Post.objects.order_by('-heart_num'):
		pics = a.picture_set.all()
		if not pics:
			continue
		pic = random.choice(pics)
		introduce_pic_list.append(pic)
		if len(introduce_pic_list) >= 4:
			break
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.all()
	print "img",img_list
	print 'aa'
	for article in article_list:
		for img in img_list:
			if img.article.title==article.title:
				print "right"
	#return render_to_response("index.html",{"article_list":article_list})
	if request.user.is_authenticated():
		mycollections_list = request.user.collector.all()
	else:
		mycollections_list = []
	slide_list=[]
	while True:
		slide_item = random.choice(img_list)
		if slide_item:
			slide_list.append(slide_item)
		if len(slide_list)>=4:
			break
	return render(request,'index.html',{"introduce_pic_list":introduce_pic_list,"introduce_list":introduce_list,'slide_list':slide_list,"article_list":article_list,"img_list":img_list,"mycollections_list":mycollections_list})
def travel(request):
	article_list = Post.objects.filter(type=0).order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.filter(type=0)
	for article in article_list:
		print article.title
	if request.user.is_authenticated():
		mycollections_list = request.user.collector.all()
	else:
		mycollections_list = []
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list,"mycollections_list":mycollections_list})

def foods(request):
	article_list = Post.objects.filter(type=1).order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.filter(type=1)
	for article in article_list:
		print article.title
	if request.user.is_authenticated():
		mycollections_list = request.user.collector.all()
	else:
		mycollections_list = []
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list,"mycollections_list":mycollections_list})
def movies(request):
	article_list = Post.objects.filter(type=3).order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.filter(type=3)
	for article in article_list:
		print article.title
	if request.user.is_authenticated():
		mycollections_list = request.user.collector.all()
	else:
		mycollections_list = []
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list,"mycollections_list":mycollections_list})
def reading(request):
	article_list = Post.objects.filter(type=2).order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.filter(type=2)
	for article in article_list:
		print article.title
	if request.user.is_authenticated():
		mycollections_list = request.user.collector.all()
	else:
		mycollections_list = []
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list,"mycollections_list":mycollections_list})
def notes(request):
	article_list = Post.objects.filter(type=4).order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.filter(type=4)
	for article in article_list:
		print article.title,article.author.id
	if request.user.is_authenticated():
		mycollections_list = request.user.collector.all()
	else:
		mycollections_list = []
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list,"mycollections_list":mycollections_list})
@login_required
def home(request,user_id):
	article_list = Post.objects.filter(author=request.user).order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.all()
	mycollections_list = request.user.collector.all()
	print article_list
	return render(request,'index.html',{"article_list":article_list,"img_list":img_list,"mycollections_list":mycollections_list})
@csrf_exempt
@login_required
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
					post.img_num +=1
					post.save()
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
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = Picture.objects.all()
	title = user.username + u"的个人信息主页"
	followers_list= user.get_followers()
	if request.user.is_authenticated():
		my_followers_list=request.user.get_followers()
	else:
		my_followers_list =[]
	print request.user
	print followers_list,'a1a2'
	followed_list = user.get_followed()
	print followed_list
	if request.user.is_authenticated():
		mycollections_list = request.user.collector.all()
	else:
		mycollections_list = []
	return render(request,'information.html',{"user":user,
											"article_list":article_list,
											"img_list":img_list,
											"title":title,
											"mycollections_list":mycollections_list,
											"followers_list":followers_list,
											"followed_list":followed_list,
											"my_followers_list":my_followers_list,
											"followers_length":len(followers_list),
											"followed_length":len(followed_list)})
@csrf_exempt
@login_required
def edit(request,user_id):
	if request.method == 'POST':
		editform =EditForm(request.POST)
		if editform.is_valid():
			request.user.username =editform.cleaned_data['username']
			request.user.email =editform.cleaned_data['email']
			request.user.mysignature =editform.cleaned_data['mysignature']
			try:
				print 'test1'
				avatar = request.FILES['file0']
				print avatar.name
				img = Image.open(avatar)
				print 'test2'
				img.thumbnail((500,500),Image.ANTIALIAS)
				name = request.user.username + '-'+ avatar.name
				for type in ['gif','jpeg','jpg','png','JPG']:
					if avatar.name.endswith(type):
						img.save("E:\\gitprojects\\myblog2\\myblog\\blog\\static\\images\\%s"%name)
						break
					else:
						print 'nonono'
			except Exception,e:
				return HttpResponse("Error %s"%e)#异常，查看报错信息
			request.user.avatar = name
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
@login_required
def follow(request,user_id):
	flag = set_follower(request.user,user_id)
	if flag:
		print u'关注成功'
	else:
		print u'关注shibai'
	return redirect(reverse('blog:get_information',args=(user_id,)))
@login_required
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
@login_required
def collect(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	article.collection.add(request.user)
	article.collection_num += 1
	article.save()
	return redirect(reverse('blog:index'))
@login_required
def no_collect(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	article.collection.remove(request.user)
	article.collection_num -= 1
	article.save()
	return redirect(reverse('blog:index'))
@login_required
def collections(request,user_id):
	article_list = request.user.collector.all().order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = []
	for article in article_list:
		img_list += Picture.objects.filter(article=article)
	return render(request,'collection_or_heart.html',{"article_list":article_list,"img_list":img_list})
@login_required
def myfollowing(request ,user_id):
	my_followers_list=request.user.get_followers()
	print my_followers_list
	return render(request,'following.html',{"my_followers_list":my_followers_list})
@login_required
def myfollowers(request,user_id):
	my_followers_list=request.user.get_followers()
	print my_followers_list
	my_followed_list = request.user.get_followed()
	print my_followed_list
	return render(request,'followers.html',{"my_followers_list":my_followers_list,"my_followed_list":my_followed_list})
@csrf_exempt
def post_detail(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	img_list = Picture.objects.filter(article =article)
	comment_list = Comment.objects.filter(article =article)
	heart_list = request.user.heart_man.all()
	commentform = CommentForm()
	messageform = MessageForm()
	return render(request,'post_detail.html',{"messageform":messageform,"article":article,"img_list":img_list,"heart_list":heart_list,'commentform':commentform,"comment_list":comment_list})
@login_required
def heart(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	article.heart.add(request.user)
	article.heart_num += 1
	article.save()
	return redirect(reverse('blog:post_detail',args=(article_id,)))
@login_required
def unheart(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	article.heart.remove(request.user)
	article.heart_num -= 1
	article.save()
	return redirect(reverse('blog:post_detail',args=(article_id,)))
@login_required
def hearts(request,user_id):
	article_list = request.user.heart_man.all().order_by('-post_time')
	page = request.GET.get('page')
	print 'page:',page
	#p = Paginator(article_list, 4)
	try:
		p = CustemPaginator(page,4,article_list, 4)
	except:
		p = CustemPaginator(1,4,article_list, 4)
	try:
		article_list = p.page(page)
	except PageNotAnInteger:
		article_list = p.page(1)
	except EmptyPage:
		article_list = p.page(p.num_pages)
	img_list = []
	for article in article_list:
		img_list += Picture.objects.filter(article=article)
	return render(request,'collection_or_heart.html',{"article_list":article_list,"img_list":img_list})
@csrf_exempt
def comment(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	if request.method == 'POST':
		commentform = CommentForm(request.POST)
		if commentform.is_valid():
			comment = Comment()
			comment.content =commentform.cleaned_data['content']
			comment.article = article
			comment.commentor = request.user
			comment.save()
			article.comment_num +=1
			article.save()
			return redirect(reverse('blog:post_detail',args=(article_id,)))
	else:
		return HttpResponse("评论失败")
@login_required
def delete(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	article.delete()
	return redirect(reverse("blog:home",args=(request.user.id,)))
@login_required
def delete_comment(request,comment_id):
	comment = get_object_or_404(Comment,pk=comment_id)
	article = comment.article
	comment.delete()
	article.comment_num -=1
	article.save()
	return redirect(reverse("blog:post_detail",args=(article.id,)))
@login_required
def send_message(request,article_id):
	article = get_object_or_404(Post,pk=article_id)
	if request.method == 'POST':
		messageform = MessageForm(request.POST)
		if messageform.is_valid():
			message = Message()
			message.content =messageform.cleaned_data['content']
			message.sender = request.user
			message.receiver = article.author
			message.save()
			return redirect(reverse('blog:post_detail',args=(article_id,)))
	else:
		return HttpResponse("私信失败")
@login_required
def messages(request,user_id):
	message_list = request.user.receiver.all()
	print message_list
	return render(request,'my_message.html',{"message_list":message_list,})
def submit_post(request):
	pass