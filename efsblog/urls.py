from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('portfolio.urls', namespace='portfolio')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^password-reset/$',password_reset,name='password_reset'),
    url(r'^password-reset/done/$',password_reset_done,name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',password_reset_confirm,name='password_reset_confirm'),
    url(r'^password-reset/complete/$',password_reset_complete,name='password_reset_complete'),
	url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
]
