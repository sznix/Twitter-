from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST

from .models import Post
from .forms import PostForm


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html', {'posts': posts, 'form': form})


@require_POST
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'post': post, 'form': form})


@require_POST
def likes(request, post_id):
    get_object_or_404(Post, id=post_id)
    Post.objects.filter(id=post_id).update(likecount=F('likecount') + 1)
    return HttpResponseRedirect('/')
