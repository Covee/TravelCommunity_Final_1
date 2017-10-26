from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('TITLE', max_length=50, null=False)
    #country = models.ForeignKey()
    content = models.TextField('CONTENT', null=False)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='upload/%Y/%m/%d/orig')
    filtered_image = models.ImageField(blank=True, null=True,
                                       upload_to='upload/%Y/%m/%d/filtered')

    # category = models.ForeignKey(Categories)
    # comments_num = models.PositiveSmallIntegerField(default=0, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
        # return reverse('korea:post_detail', args=(self.id,))

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Post, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('korea:post_detail', args={self.id})
