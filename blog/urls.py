from django.urls import path
from . import views
from .views import ArticleDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('category/<str:category>/', views.category, name='category'),
    path('search/', views.search, name='search'),
]
