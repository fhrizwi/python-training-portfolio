from django.http import request,HttpResponse
from django.shortcuts import render
import json
import os
from django.conf import settings

def load_json_data(filename):
    """Helper function to load JSON data"""
    file_path = os.path.join(settings.BASE_DIR, 'data', filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def home(request):
    # Load data from JSON files
    projects_data = load_json_data('projects.json')
    skills_data = load_json_data('skills.json')
    blog_data = load_json_data('blog.json')
    
    context = {
        'featured_projects': projects_data.get('featured_projects', [])[:3],
        'skills': skills_data.get('skills', []),
        'latest_blogs': blog_data.get('blog_posts', [])[:3],
    }
    return render(request, 'home.html', context)

def about(request):
    skills_data = load_json_data('skills.json')
    context = {
        'skills': skills_data.get('skills', []),
    }
    return render(request, 'about.html', context)

def blog(request):
    blog_data = load_json_data('blog.json')
    context = {
        'blog_posts': blog_data.get('blog_posts', []),
    }
    return render(request, 'blog.html', context)


def contact(request):
    return render(request, 'contact.html')

