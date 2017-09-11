from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def ask_post(request):
    if request.method == "GET":
        form = PostForm(request.POST)
        return render(request, 'blog/post_list.html', {'form':form})
    elif request.method == "POST":
        #post = Post.objects.filter(title=request.POST['title'])
        post = get_object_or_404(Post, title=request.POST['title'])
        if not post:
            form = PostForm(request.POST)
            return render(request, 'blog/post_list.html', {'form':form})
        else:
             #form = PostForm(instance=post[0])
             form = PostForm(instance=post)
             return render(request, 'blog/post_list.html', {'form':form})

