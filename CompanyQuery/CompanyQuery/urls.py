"""CompanyQuery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from query import views
from django.conf.urls import url

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('StockBasic', views.StockBasic, name = 'StockBasic'),
    path('GetLawCase', views.GetLawCase, name = 'GetLawCase'),
    path('GetStock', views.GetStock, name = 'GetStock'),
    path('Login', views.Login, name = 'Login'),
    path('Modify', views.Modify, name = 'Modify'),
    path('Delete', views.Delete, name='Delete'),
    path('Insert', views.Insert, name='Insert'),

]
