from django.urls import path, include
from .views import PostListView, SinglePostView, PostCreateView

urlpatterns = [

    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/', SinglePostView.as_view(), name='post_detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
]