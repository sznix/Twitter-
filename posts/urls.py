from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('likes/<int:post_id>/', views.likes, name='like'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
]
