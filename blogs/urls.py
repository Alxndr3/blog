"u""Defines URL patterns for Blogs"""
from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
        # Home page
        path('', views.index, name='index'),
        path('posts/', views.posts, name='posts'),
        path('posts/<int:post_id>/', views.post, name='post'),
        path('new_post/', views.new_post, name='new_post'),
        path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
        ]
