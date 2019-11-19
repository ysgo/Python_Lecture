from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

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
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    return render(request, 'articles/detail.html', {'article':article, 'comments':comments, 'comment_form':comment_form, 'person':person})

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
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article_id)
    #     return redirect('articles:detail', article.id)
    # else:
    #     return redirect('articles:detail', article_id)

@login_required
def comment_delete(request, article_id, comment_id):
    # if request.method == 'POST':
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('articles:detail', article_id)

@login_required
def like(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = request.user
    # 해당 게시글에 좋아요를 누른 사람들 중에서 user.id(현재 접속유저의 id)를 가진 user가 존재하면
    if article.like_users.filter(pk=user.id).exists():
        # user를 삭제한다(좋아요를 취소)
        article.like_users.remove(user)
    else:
        # user가 존재하지 않는다면 user를 추가한다.
        article.like_users.add(user)
    return redirect('articles:index')

def follow(request, article_id, user_id):
    # 게시글 유저
    you = get_object_or_404(get_user_model(), pk=user_id)
    # 접속 유저
    me = request.user
    if you != me:
        if you.followers.filter(pk=me.pk).exists(): # 게시글을 작성한 유저의 팔로워 목록에 내 계정이 있는 경우의 조건
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('articles:detail', article_id)
