# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from sblog.models import Blog, Author

# Create your views here.

def index(request):
	userinfo = Author.objects.all()
	blogs = Blog.objects.all()
	return render(request, "sblog/blog_list.html", {'userinfo': userinfo, 'blogs': blogs})

def article(request, blog_id=''):
	blog_content = Blog.objects.get(id=blog_id)
	return render(request, 'sblog/blog_detail.html', {'blog_content': blog_content})