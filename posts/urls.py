from django.urls import path, include
from .views import PostDeleteView, PostListView, SinglePostView, PostCreateView, PostUpdateView

urlpatterns = [

    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/', SinglePostView.as_view(), name='post_detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('update_post/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('del_post/<int:pk>', PostDeleteView.as_view(), name='del_post'),

]