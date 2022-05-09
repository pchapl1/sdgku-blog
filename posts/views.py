from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .forms import PostForm
from .models import Post

class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    template_name = 'all_posts.html'
    model = Post
    context_object_name = 'posts'


class SinglePostView(LoginRequiredMixin, DetailView):
    template_name = 'single_post.html'
    model = Post
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'confirm_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self) -> str:
        return reverse_lazy('posts')