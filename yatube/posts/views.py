from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Group
from .forms import PostForm
from .utils import paginate


def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.select_related('group', 'author').all()

    context = {
        'title': title,
        'page_obj': paginate(posts, request),
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()

    context = {
        'group': group,
        'page_obj': paginate(posts, request),
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    title = 'Профайл пользователя ' + author.get_full_name()
    posts = author.posts.all()
    post_count = posts.count()

    context = {
        'title': title,
        'author': author,
        'post_count': post_count,
        'page_obj': paginate(posts, request),
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = get_object_or_404(User, username=post.author)
    post_count = author.posts.count()
    title = 'Пост ' + post.text[:30]
    context = {
        'title': title,
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            return redirect('posts:profile', request.user)
    form.fields['text'].help_text = 'Текст нового поста'
    context = {
        'form': form,
        'is_edit': False,
    }
    return render(request, 'posts/create_post.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_id)
    else:
        form = PostForm(instance=post)
    form.fields['text'].help_text = 'Текст поста'
    context = {
        'form': form,
        'is_edit': True,
        'post_id': post_id
    }
    return render(request, 'posts/create_post.html', context)
