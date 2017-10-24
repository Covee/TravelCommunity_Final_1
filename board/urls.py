from django.conf.urls import url, include
from board.views import *


urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^korea/', KoreaBoard.as_view(), name='korea'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail')

]

#static(settings.MEDIA.URL, document_root = settings.MEDIA_ROOT)
