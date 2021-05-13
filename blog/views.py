from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post

# Create your views here.

class PostList(ListView): # to get list of posts
    model = Post # model data


class PostCreateView(CreateView): # form for create-post
    model = Post
    fields = ('title', 'description', 'image', 'created_at', )
    template_name = 'blog/post_create.html'
    success_url = '/blog' # redirect when create-post is success 

    def form_valid(self, form): # get author by default
        form.instance.author = self.request.user
        return super().form_valid(form)