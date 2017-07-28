#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^article/(?P<blog_id>[0-9])/$', views.article, name='article'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)