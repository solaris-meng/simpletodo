"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^$', todo_user_view, name='todo_user_view'),
    url(r'^import$', todo_import_view, name='todo_import_view'),
    url(r'^add$', todo_add_handler, name='todo_add_handler'),
    url(r'^import_handler$', todo_import_handler, name='todo_import_handler'),
    url(r'^(?P<tid>[\w\W]+)/(?P<opt>[\w\W]+)$', todo_update_handler, name='todo_update_handler'),
    # log
]
