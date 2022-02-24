from django.urls import path, include
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('posts/<int:pk>', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view() ,name='new_post'),
    path('posts/<int:pk>/edit/', views.BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete')
]