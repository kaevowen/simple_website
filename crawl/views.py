from django.shortcuts import render
from django.http import HttpResponse
from . import parser
from django.template.loader import render_to_string


def crawl(req):
    ctx = parser.crawl_naver_news()
    return render(req, 'crawl/result.html', ctx)


def refresh(req):
    ctx = parser.crawl_naver_news()
    a = render_to_string('crawl/refresh_format.html', ctx)
    return HttpResponse(a)

# Create your views here.
