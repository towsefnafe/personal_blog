from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count

def categories():
    all_categories = Category.objects.all().annotate(Count('post'))
    return all_categories

def latest_post():
    latest_post_list_obj = Post.objects.all()[::-1][:5]
    return latest_post_list_obj

def home(request):
    post_obj = Post.objects.all()[::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(post_obj, 10)
    category = categories()
    lastest_post_obj = latest_post()
    user = User.objects.all()[0]
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    context = {
        'cases': cases,
        'categories': category,
        'lastest_post_obj': lastest_post_obj,
        'user': user,
    }
    return render(request, 'blog/index.html', context)

def about(request):
    user = User.objects.all()[0]
    category = categories()
    context = {
        'user': user,
        'categories': category,
    }
    return render(request, 'blog/about.html', context)

def contact(request):
    user = User.objects.all()[0]
    category = categories()
    context = {
        'user': user,
        'categories': category,
    }
    return render(request, 'blog/contact.html', context)

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

    def get_context_data(self, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        lastest_post_obj = latest_post()
        category = categories()
        user = User.objects.all()[0]
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['categories'] = category
        context['lastest_post_obj'] = lastest_post_obj
        context['user'] = user
        return context

def category(request, category):
    post_obj = Post.objects.filter(category__name=category.replace('-', ' '))[::-1]
    lastest_post_obj = latest_post()
    category = categories()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_obj, 10)
    user = User.objects.all()[0]
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    context = {
        'cases': cases,
        'categories': category,
        'lastest_post_obj': lastest_post_obj,
        'user': user,
    }
    return render(request, 'blog/index.html', context)

def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        post_obj = Post.objects.filter(title__contains=search_term)[::-1]
        lastest_post_obj = latest_post()
        category = categories()
        page = request.GET.get('page', 1)
        paginator = Paginator(post_obj, 10)
        user = User.objects.all()[0]
        try:
            cases = paginator.page(page)
        except PageNotAnInteger:
            cases = paginator.page(1)
        except EmptyPage:
            cases = paginator.page(paginator.num_pages)
        context = {
            'cases': cases,
            'categories': category,
            'lastest_post_obj': lastest_post_obj,
            'user': user,
        }
        return render(request, 'blog/index.html', context)
