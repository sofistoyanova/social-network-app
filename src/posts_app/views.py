from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from comments_app.models import Comment
from comments_app.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/signin/')
def create_post(request):
    return render(request, 'post_create.html')


@login_required(login_url='/auth/signin/')
def update_post(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'post_update.html', context)


def post_list(request):
    return render(request, 'post_list.html')


def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'post_details.html', context)
