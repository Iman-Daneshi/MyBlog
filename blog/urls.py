from django.urls import path
from .views import index_view, single_post

app_name = 'blog'
urlpatterns = [
    path('', index_view, name='index'),
    path('<str:id>', single_post, name='single_post'),
]
