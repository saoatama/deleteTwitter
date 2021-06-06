from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('continue_delete/', views.continue_delete, name='continue_delete'),
]
