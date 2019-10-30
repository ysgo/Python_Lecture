from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html', {'articles':articles})

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.svae()

    # 2번째 방법
    article = Article(title=title, content=content)
    article.save()

    # 3번째 방법
    # Article.objects.crate(title=title, content=content)
    #return render(request, 'articles/create.html')
    return redirect(f'/articles/{article.pk}/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html', {'article':article})