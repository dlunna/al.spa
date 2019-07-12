from django.urls import path
from . import views
from .views import cubaListView, cubaDetailView, cubaCreateView

cubas_patterns = ([
    path('', cubaListView.as_view(), name='cubas'),
    path('<int:pk>/<slug:slug>/', cubaDetailView.as_view(), name='cuba'),
    path('create/', cubaCreateView.as_view(), name='create'),

], 'cubas')