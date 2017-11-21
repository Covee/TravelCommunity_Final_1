# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.

from ..models import Comment, Post
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def create_comment(request):
    """
    comment 생성
    """
    user_id = request.POST.get('user_id')
    post = request.POST.get('post')
    message = request.POST.get('message')

    Comment.objects.create(
        post=Post.objects.get(id=post),
        user=User.objects.get(username=user_id),
        message=message,
        approved_comment=True
    )

    return Response({
        'success': True,
    })


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def list_up_comment(request):
    """
    comment 조회
    """
    id = request.POST.get('id')
    comments = Comment.objects.filter(post=id).values_list('id', 'approved_comment', 'created_at', 'message', 'user__username')
    data = []

    for id, auth, ctime, message, user in comments:
        data.append({
            'id': id,
            'auth': auth,
            'ctime': ctime,
            'message': message,
            'user_id': user
        })

    return Response({
        'success': True,
        'data': data
    })


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def del_comment(request):
    """
    comment 삭제
    """
    id = request.POST.get('id')
    comments = Comment.objects.get(id=id)
    comments.delete()

    return Response({
        'success': True,
    })


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def update_comment(request):
    """
    comment 삭제
    """
    id = request.POST.get('id')
    comments = Comment.objects.get(id=id)
    comments.delete()

    return Response({
        'success': True,
    })


