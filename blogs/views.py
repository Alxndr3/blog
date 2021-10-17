from django.shortcuts import render, redirect
from django.http import Http404
from .models import BlogPost
from .forms import PostForm


def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all posts."""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """Show details of an individual post."""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)

def new_post(request):
    """Add a new post."""
    if request.method !='POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')
    # Display a blank or invalida form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request: pre-fill form with the current post.
        form = PostForm(instance=post)
    else:
        # POST data submited; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

