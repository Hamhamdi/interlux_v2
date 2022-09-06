from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [


    # path('', views.General_db, name="home" ),
    # path('logout/', views.logoutUser, name="logout" ),
    # path('login/', views.loginPage, name="login" ),
    # path('register/', views.registerPage, name="register" ),
    # # path('respo_log1/', views.rl1Page, name="respo_log1" ),
    # # path('respo_log2/', views.rl2Page, name="respo_log2" ),
    # # path('respo_info/', views.rinfoPage, name="respo_info" ),
    # # path('respo_fin/', views.rfinPage, name="respo_fin" ),
    # # path('respo_ca/', views.RCa, name="respo_ca" ),
    # path('respo_ca_add/', views.addRCa, name="respo_ca_add" ),
    # # path('general_db/', views.General_db, name="general_db" ),


    path('', views.home, name="home" ),
    path('logout/', views.logoutUser, name="logout" ),
    path('login/', views.loginPage, name="login" ),
    path('register/', views.registerPage, name="register" ),
    path('respo_log1/', views.rl1Page, name="respo_log1" ),
    path('respo_log2/', views.rl2Page, name="respo_log2" ),
    path('respo_info/', views.rinfoPage, name="respo_info" ),
    path('respo_fin/', views.rfinPage, name="respo_fin" ),
    path('respo_ca/', views.RCa, name="respo_ca" ),
    path('respo_ca_add/', views.addRCa, name="respo_ca_add" ),
    path('general_db/', views.General_db, name="general_db" ),


]