from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


from .models import Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForms
from django.contrib.auth.mixins import LoginRequiredMixin


class PostAuth(LoginRequiredMixin, TemplateView):
    form_class = PostForms
    model = Post


class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now']=datetime.utcnow()
        context['next_sale']=None
        context['filterset']=self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForms
    model = Post
    template_name = 'post_edit.html'
    context_object_name = 'create'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == 'news/articles/create/':
            post.post_news = 'SE'
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForms
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')


class PostSearch(ListView):
    model = Post
    ordering = '-date'
    template_name = 'post.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesCreate(CreateView):
    permission_required = 'news.add_post'
    from_class = Post
