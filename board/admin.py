from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_posts = ('title', 'id', 'modify_date')
	list_filter = ('modify_date',)
	search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
