from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def index(request):
    articles = Article.objects.order_by('-pk')
    # articles = Article.objects.all()[::-1]
    return render(request, 'articles/index.html', {'articles':articles})

# def new(request):
#     return render(request, 'articles/new.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # image = request.FILES.get('image')
            # article = Article(title=title, content=content, image=image)
            # article.save()
            return redirect('articles:detail', article.id)
    else:
        return render(request, 'articles/new.html')

# @require_POST
def detail(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    return render(request, 'articles/detail.html', {'article':article, 'comments':comments, 'comment_form':comment_form})

@login_required
@require_POST
def delete(request, article_id):
    # article = Article.objects.get(pk=article_id)
    # if request.method == 'POST':
    article = get_object_or_404(Article, pk=article_id)
    if article.user == request.user:
        article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     return render(request, 'articles/edit.html', {'article':article})

@login_required
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.id)
            # article.title = request.POST.get('title')
            # article.content = request.POST.get('content')
            # article.image = request.FILES.get('image')
            # article.save()
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    return render(request, 'articles/form.html', {'form':form, 'article':article})

@require_POST
def comment_create(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    comment_form = CommentForm(request.POST)
    # if request.method == 'POST':
    #comment = Comment()
    #comment.content = request.POST.get('content')
    comment = comment_form.save(commit=False)
    comment.article = article
    comment.save()
    #     return redirect('articles:detail', article.id)
    # else:
    #     return redirect('articles:detail', article_id)
    return redirect('articles:detail', article_id)

@require_POST
def comment_delete(request, article_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
    return redirect('articles:detail', article_id)