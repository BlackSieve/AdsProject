from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch, CategoryListView, subscribe
from sign.views import ConfirmUser

urlpatterns = [
    path('post/', PostList.as_view(), name = 'post-list'),
    path('post/<int:pk>/', PostDetail.as_view(), name = 'post-detail'),
    path('post/search/', PostSearch.as_view(), name = 'post-search'),
    # path('ads/create/', PostCreate.as_view(), name = 'ads-create'),
    # path('ads/<int:pk>/edit/', PostUpdate.as_view(), name='ads-edit'),
    # path('ads/<int:pk>/delete/', PostDelete.as_view(), name='ads-delete'),
    path('ads/create/', PostCreate.as_view(), name = 'articles-create'),
    path('ads/<int:pk>/edit/', PostUpdate.as_view(), name = 'articles-edit'),
    path('ads/<int:pk>/delete/', PostDelete.as_view(), name = 'articles-delete'),
    path('categories/<int:pk>/',CategoryListView.as_view(), name = 'category-list'),
    path('categories/<int:pk>/subscribe/', subscribe, name = 'subscribe'),
    path('confirm/',ConfirmUser.as_view(),name = 'confirm_user')
    ]