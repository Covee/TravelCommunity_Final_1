from django.conf.urls import url, include
from board.views import *


urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^board/', korea_board.as_view(), name='korea'),
    #url(r'^board/post_detail/', PostDetail.as_view(), name='post_detail')
]
