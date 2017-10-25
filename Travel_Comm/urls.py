from django.conf.urls import url, include
from django.contrib import admin

from Travel_Comm.views import HomeView
from .views import UserCreateView, UserCreateDoneView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^board/', include('board.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneView.as_view(), name='register_done')
    
]
