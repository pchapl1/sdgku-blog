from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm


class PostListView(ListView):
    template_name = 'all_posts.html'
    model = Post
    context_object_name = 'posts'


class SinglePostView(DetailView):
    template_name = 'single_post.html'
    model = Post
    context_object_name = 'post'