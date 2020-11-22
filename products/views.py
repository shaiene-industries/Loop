from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Class views
class PostsView(ListView):
    model = Post
    template_name = "posts/home.html"

class ArticleView(DetailView):
    model = Post
    template_name = "posts/articleDetail.html"


class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/postForm.html'
    form_class = PostForm
    login_url = 'accounts/login/'

    # Overriding form_valid to associate the user to the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#Function Views
# def base(request):
#     return render(request,'base/base.html',{})

# def home(request):
#     return render(request,'home.html', {})
