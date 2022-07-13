"""stockmarketwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
# from django.conf.urls import url
from django.urls import re_path as url
from firstPage import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.index,name='Homepage'),
    url('analysis',views.analysis,name='analysis'),
    url('predictValue',views.predictValue,name='predictValue'),
    url('login',views.login,name='login'),
    url('validateRegisterCredentials',views.login,name='validateRegisterCredentials'),
    url('validateLoginCredentials',views.login,name='validateLoginCredentials'),
]
urlpatterns += staticfiles_urlpatterns()
