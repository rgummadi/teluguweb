from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.mainsite.queries import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def news(request, paper=''):
    link_list = get_links(paper)
    print(paper)
    paginator = Paginator(link_list, 40)

    page = request.GET.get('page')

    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        links = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        links = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {"links": links})