from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField('CONTENT', null = False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse('korea:post_detail', args=(self.id,))