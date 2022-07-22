from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
from django.urls import re_path as url
from firstPage import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import path, include
urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$',views.index,name='Homepage'),
    url('analysis',views.analysis,name='analysis'),
    url('predictValue',views.predictValue,name='predictValue'),
    url('loginuser',views.login,name='login'),
    url('validateRegisterCredentials',views.validateRegisterCredentials,name='validateRegisterCredentials'),
    url('validateLoginCredentials',views.validateLoginCredentials,name='validateLoginCredentials'),
    url('controlpanel',views.controlpanel,name='controlpanel'),
    url('search',views.controlpanel,name='controlpanel'),
    url('accounts/', include('allauth.urls')),
    url("logout", views.logout_request, name= "logout"),
]
urlpatterns += staticfiles_urlpatterns()
