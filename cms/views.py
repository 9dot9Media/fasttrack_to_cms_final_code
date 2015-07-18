from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Article, Category, Image, Gallery, Tag


def home(request):
    articles = Article.objects.filter(publish_status=True)[:10]
    categories = Category.objects.annotate(
        num_articles=Count('article')
    ).order_by('-num_articles')[:2]

    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'cms/home.html', context)


class ArticleDetail(DetailView):
    queryset = Article.objects.filter(
        publish_status=True)


class ArticleList(ListView):
    queryset = Article.objects.filter(
        publish_status=True)


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category


class TagList(ListView):
    queryset = Tag.objects.annotate(
        num_articles=Count('article'))


class TagDetail(DetailView):
    model = Tag


class GalleryList(ListView):
    model = Gallery


class GalleryDetail(DetailView):
    model = Gallery

    def get_template_names(self):
        if self.object.layout == 'HORI':
            return ('cms/gallery_detail_horizontal.html',)
        elif self.object.layout == 'VERT':
            return ('cms/gallery_detail_vertical.html',)
        else:
            return ('cms/gallery_detail_links.html',)


class AuthorList(ListView):
    model = User


class AuthorDetail(DetailView):
    model = User

    def get_slug_field(self):
        return 'username'


class ImageDetail(DetailView):
    model = Image
