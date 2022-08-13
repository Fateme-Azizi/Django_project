# from django.contrib import admin
from django.urls import path
# from . import views
from .views import PostListView
from . import views

urlpatterns = [
    # path("view/", PostListView.as_view(), name="blog-view"),
    path("home/", views.home, name='home')
]
