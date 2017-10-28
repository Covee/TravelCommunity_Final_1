from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Travel_Comm.views import HomeView, CreateUserView, RegisteredView
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^board/', include('board.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('allauth.urls')),


]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

