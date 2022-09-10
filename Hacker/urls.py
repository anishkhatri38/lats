from django.contrib import admin
from django.urls import path
from . import views
# for password reset
from django.contrib.auth import views as auth_views

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [   
    # Added 
    # path('', views.index, name = 'index'),
    path('projects', views.projects, name = 'projects'),
    path('project-obj/<str:pk>/', views.project, name = 'project'),
    path('create-project/', views.createProject, name = 'create-project'),
    path('update-project/<str:pk>/', views.updateProject, name = 'update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name = 'delete-project'),






    # Added later for Trainer Room 
    path('', views.index, name = 'index'),
    path('communicate/', views.communicate, name = 'communicate'),
    path('room/<str:pk>/', views.room, name = 'room'),
    path('profile/<str:pk>/', views.customerProfile, name ='customer-profile'),
    # path ('profile/<str:pk>/', views.userProfile, name = "user-profile"),
    
    path('create-room/', views.createRoom, name = "create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name = "update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name = "delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name = "delete-message"),

    path('update-user', views.updateUser, name = "update-user"),
    path('login-customer/', views.loginCustomer, name = 'login-customer'),
    path('register-customer/', views.registerCustomer, name = 'register-customer'),
    ## for flexible device design 
    path('topics/', views.topicsPage, name = 'topics'),
    path('activity/', views.activityPage, name = 'activity'),


    ## this is for footer 
    path('about/', views.AboutUs, name = 'about'),
    
    # for membership of the program 
    path('membership/', views.userMembership, name = 'membership'),
    path('checkout/', views.userCheckout, name = 'checkout'),

    # for customer rendering 
    path('project-customer', views.projectsCustomer, name = 'project-customer'),

    # for inbox
    # path ('create-message/', views.createMessage, name = "create-message"),

]


