from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def root(request):
    posts = Post.objects.all()
    return render(request, "blog/morty.html",{'posts':posts})

def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, "blog/category.html", {'category':category,
                                                  'posts':posts
                                                  })

def categori(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    return render(request, "blog/categori.html", {'category':category,
                                                  'posts':posts
                                                  })


def cat3gory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    allcategory = Category.objects.all()
    return render(request, "blog/cat3gory.html", {'category':category,
                                                  'allcategory':allcategory,
                                                  })