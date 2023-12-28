from django.urls import path
from . import views

urlpatterns = [
    path('atashfeshan/', views.atashfeshan_slide, name='atashfeshan'),
    path('', views.main_page, name='mainPage'),
    path('search/', views.search_slide, name='search'),
]
