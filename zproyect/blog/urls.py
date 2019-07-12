from django.urls import path
from . import views as blog_views


urlpatterns = [

    path('', blog_views.root, name="blog"),
    path('cat3gory/', blog_views.categori, name="categori"),
    path('category/<int:category_id>/', blog_views.category, name="category"),
    path('cat3gory/<int:category_id>/', blog_views.cat3gory, name="cat3gory"),
]


