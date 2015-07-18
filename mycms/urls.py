"""mycms URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

from cms import views
from mycms import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home, name='home'),

    url(r'^articles/$', views.ArticleList.as_view(), name='articles-list'),
    url(r'^articles/(?P<slug>[\w-]+)$', views.ArticleDetail.as_view(), name='articles-detail'),

    url(r'^categories/$', views.CategoryList.as_view(), name='categories-list'),
    url(r'^categories/(?P<slug>[\w-]+)$', views.CategoryDetail.as_view(), name='categories-detail'),

    url(r'^tags/$', views.TagList.as_view(), name='tags-list'),
    url(r'^tags/(?P<slug>[\w-]+)$', views.TagDetail.as_view(), name='tags-detail'),

    url(r'^galleries/$', views.GalleryList.as_view(), name='galleries-list'),
    url(r'^galleries/(?P<slug>[\w-]+)$', views.GalleryDetail.as_view(), name='galleries-detail'),

    url(r'^authors/$', views.AuthorList.as_view(), name='authors-list'),
    url(r'^authors/(?P<slug>[\w-]+)$', views.AuthorDetail.as_view(), name='authors-detail'),

    url(r'^image/(?P<slug>[\w-]+)$', views.ImageDetail.as_view(), name='image-detail'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

]
