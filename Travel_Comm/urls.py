from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Travel_Comm.views import HomeView, CreateUserView, RegisteredView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^board/', include('board.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', CreateUserView.as_view(), name='register'),
    url(r'^accounts/register/done/$', RegisteredView.as_view(), name='register_done'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.login, name='logout'),
]
