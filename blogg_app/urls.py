from django.urls import path, include
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('posts/<int:pk>', views.BlogDetailView.as_view(), name='posts'),
]