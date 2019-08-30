from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def root(request):
    posts = Post.objects.all()
    return render(request, "blog/fifi.html",{'posts':posts})
    #return render(request, "blog/services.html",{'posts':posts})

def morty(request):
    posts = Post.objects.all()
    return render(request, "blog/morty.html",{'posts':posts})

def categori(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    return render(request, "blog/categori.html", {'category':category,
                                                  'posts':posts
                                                  })

# Esta es la forma rudimentaria de hacer las consultas
def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    #Se le va a pasar la categoria y luego el filtro
    category = get_object_or_404(Category, id=category_id)
    #Para que haga una consulta en base a category que
    #recuperamos antes
    posts = Post.objects.filter(categories=category)
    return render(request, "blog/category.html", {'category':category,
                                                  'posts':posts
                                                  })

def cat3gory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    allcategory = Category.objects.all()
    return render(request, "blog/cat3gory.html", {'category':category,
                                                  'allcategory':allcategory,
                                                  })


