from django.urls import path
from .views import PostListCreateView, PostDetailView, PostFilterView, LikeListView, LikeDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/filter/<str:name>/', PostFilterView.as_view(), name='post-filter'),
    path('likes/', LikeListView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail')
]