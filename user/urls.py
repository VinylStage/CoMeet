from django.urls import path
from user import views

urlpatterns = [
    path('log_in/', views.log_in_view, name='log_in'),  #태연
    path('logout/', views.logout, name='logout'),   #태연
    path('sign_up/', views.sign_up_view, name='sign_up'),  #태연
]
"""
디테일 페이지
"""
