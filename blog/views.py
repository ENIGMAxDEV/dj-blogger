from django.shortcuts import render, get_object_or_404
from .models import Post



def home(r):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': Post.objects.all()
    }
    return render(r, 'index.html', context)


def about(r):
    context = {
        'title': 'من أنا',
    }
    return render(r, 'about.html', context)


def post_details(r, post_id):
    post = get_object_or_404(Post, pk = post_id)
    context = {
        'post': post,
    }
    return render(r, 'post_detail.html', context)
