from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.commit, name='main'),
    path('write-view/', views.write_view, name='write-view')
]
