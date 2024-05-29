"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='home'),

    path('login/', views.login, name ='login'),
    path('act1/', views.act1, name ='act1'),
    path('act2/', views.act2, name ='act2'),
    path('act3/', views.act3, name ='act3'),
    path('act4/', views.act4, name ='act4'),
    path('act5/', views.act5, name ='act5'),
    path('act6/', views.act6, name ='act6'),
    path('contact/', views.contact, name ='contact'),
    path('dashboard/', views.dashboard, name ='dashboard'),


]
