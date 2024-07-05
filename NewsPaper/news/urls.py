from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch

urlpatterns = [
    path('post/', PostList.as_view(), name = 'post-list'),
    path('post/<int:pk>/', PostDetail.as_view(), name = 'post-detail'),
    path('post/search/', PostSearch.as_view(), name = 'post-search'),
    path('news/create/', PostCreate.as_view(), name = 'news-create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news-edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news-delete'),
    path('articles/create/', PostCreate.as_view(), name = 'articles-create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name = 'articles-edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name = 'articles-delete'),
    ]