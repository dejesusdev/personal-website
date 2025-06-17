from django.shortcuts import render
from .models import Project, Photo
from .models import BlogPost
from django.views.generic import ListView

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def tech(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # newest first
    return render(request, 'tech.html', {'title': 'Tech'})

def ghs(request):
    photo_filenames = [f"ghs{i}.jpg" for i in range(1, 113)]
    return render(request, "ghs.html", {"title": "DIY Projects", "photo_filenames": photo_filenames})

def photography(request):
    photo_filenames = [f"photograph{i}.jpg" for i in range(1, 21)]  # 1 to 20 inclusive
    return render(request, "photography.html", {"title": "Photography", "photo_filenames": photo_filenames})

class TechView(ListView):
    model = BlogPost
    template_name = 'tech.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # newest first