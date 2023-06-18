from django.urls import path, include
from .views import about, home, PostListView, PostDetailView, portfolio

urlpatterns = [
    path("", home),
    path("about/", about),
    path("blog/", PostListView.as_view()),
    path("blog/<int:pk>", PostDetailView.as_view()),
    path("portfolio/", portfolio)
]
