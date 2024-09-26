from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters import FilterSet
from news.models import Comment, Post


class PostFilter(FilterSet):
    class Meta:
        model = Comment
        fields = [
            'post'
        ]

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(user_id=kwargs('request'))


class IndexView(LoginRequiredMixin, TemplateView):
    model = Comment
    template_name = 'protect/index.html'
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = Comment.objects.filter(post__author__user_id=self.request.user.id)
        self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Comment.objects.none()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
