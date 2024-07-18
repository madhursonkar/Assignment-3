from django.contrib import admin
from django.urls import path
from members import views


urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login_,name='login'),
    path('signup',views.signup_,name='signup'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
]
