from django.shortcuts import render
from django.views import generic
from .models import Post

# Class inheriting from Generic ListView
class PostList(generic.ListView):
    model = Post
    # Only published Posts visible to Users ergo 1
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # Renders on the index.html
    template_name='index.html'
    # Separates the number of Posts by 6
    paginate_by = 6