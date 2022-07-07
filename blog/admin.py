from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'status', 'published_date', 'created_date', 'updated_date')
    list_filter  = ('status', 'author',)
    ordering = ['-created_date',]
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
