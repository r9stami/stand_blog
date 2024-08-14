from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>',views.PostDetailView.as_view(),name='post_detail'),
    path('comment/<slug:slug>',views.CommentCreateView.as_view(),name='comment'),
    path('like/<slug:slug>/<int:pk>',views.LikePostView.as_view(),name='like'),
    path('list',views.PostListView.as_view(),name='post_list'),
    path('search/post',views.SearchPostView.as_view(),name='search'),
    path('category/detail/<int:id>',views.CategoryDetailView.as_view(),name='category'),
]