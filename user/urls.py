from django.urls import path
from . import views

urlpatterns = [
    path('log_in/', views.log_in_view, name='log_in'),
    path('log_out/', views.log_out_view, name='log_out'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('my_page/', views.my_page_view, name='my_page'),
]

