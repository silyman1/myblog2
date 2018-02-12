from django.contrib import admin
from .models import User,Post,Picture,Friendship,Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Picture)
admin.site.register(Friendship)
admin.site.register(Comment)