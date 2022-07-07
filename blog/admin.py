from django.contrib import admin
from blog.models import Post, Review, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'status', 'published_date', 'created_date', 'updated_date')
    list_filter  = ('status', 'author',)
    ordering = ['-created_date',]
    search_fields = ['title', 'content']

class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('value', 'created_date', 'updated_date')
    list_filter  = ('value',)
    ordering = ['-created_date',]
    search_fields = ['value',]

admin.site.register(Post, PostAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag)

