from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('detail/<int:id>',views.detail_commit,name='detail_commit'),
    path('detail/comment/<int:id>', views.detail_write_comment, name='detail_writer_comment'),
    path('detail/comment/delete/<int:id>',views.detail_delete_comment, name='detail_delete-comment'),
]