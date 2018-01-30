#--coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm
# Create your views here.
@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			username =loginform.cleaned_data['username']
			password =loginform.cleaned_data['password']
			user = authenticate(username=username,password=password)
			print user
			if user:
				login(request,user)
			return render_to_response('login.html',{'loginform':loginform})
	else:
		loginform = LoginForm()
		return render_to_response('login.html',{'loginform':loginform})
@login_required
def index(request):
	#article_list = get_object_or_404
	article_list={}
	return render_to_response("index.html",{"article_list":article_list})
def home(request):
	return HttpResponse("hello")