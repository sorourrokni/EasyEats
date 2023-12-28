from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def atashfeshan_slide(request):
    template = loader.get_template('atashfeshan.html')
    return HttpResponse(template.render())


def main_page(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())


def search_slide(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())
