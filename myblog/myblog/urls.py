from django.conf.urls import include, url
from django.contrib import admin
from blog.views import login_view,logout_view,echo,ajax_test_add
urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls',namespace="blog")),
    url(r'^accounts/login/$', login_view),
    url(r'^accounts/logout/$', logout_view),
    url(r'^search/$', include('haystack.urls')),
    url(r'^echo$', echo),
	url(r'^ajax/add/',ajax_test_add, name = 'ajax_test_add'),
]
