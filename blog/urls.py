from django.urls import path
from . views import PostList, PostCreateView

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    
]