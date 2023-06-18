from django.shortcuts import render
from . import models
from .models import About, Post, SocialLink, ProfileData, Tool, Category, Project
from django.views import generic

# Create your views here.#


def home(request):
    profile = models.ProfileData.objects.first()
    tools = models.Tool.objects.all().order_by("order")
    social_links = models.SocialLink.objects.all().order_by('order')
    about = About.objects.last()
    services = models.Service.objects.all().order_by('order')
    categories = models.Category.objects.all()
    projects = models.Project.objects.all()[:4]
    posts = models.Post.objects.all()[:4]

    context = {
            "profile": profile,  # 1 dona
            "tools": tools,  # query set
            "social_links": social_links,
            "about": about,
            "services": services,
            "categories": categories,
            "projects": projects,
            "posts": posts,
               }

    return render(request, 'index.html', context)


def about(request):
    about = About.objects.last()
    tools = Tool.objects.all()

    context = {
        "about": about,
        "tools": tools,
    }
    return render(request, "about-us.html", context)


def portfolio(request):
    categories = Category.objects.all(),
    projects = Project.objects.all(),

    context = {
        "categories": categories,
        "projects": projects,
    }

    return render(request, "portfolio.html", context)


class PostListView(generic.ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        popular_posts = Post.objects.all().order_by("-views_count")[:4]
        context["popular_posts"] = popular_posts
        social_links = SocialLink.objects.all().order_by("order")
        context['social_links'] = social_links
        profile_data = ProfileData.objects.first()
        context["profile_data"] = profile_data
        return context

    def get_queryset(self):
        search = self.request.GET.get("search", "")
        queryset = super().get_queryset()

        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "single-blog.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        social_links = SocialLink.objects.all().order_by("order")
        context["links"] = social_links
        profile_data = ProfileData.objects.first()
        context["blog"] = profile_data
        popular_posts = Post.objects.all().order_by("-views_count")[:4]
        context["most_watched_posts"] = popular_posts

        return context
