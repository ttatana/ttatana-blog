from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/like/', views.post_like, name='post_like'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('image/<int:pk>/delete/', views.delete_image, name='delete_image'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup'),
]