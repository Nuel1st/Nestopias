from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Renders an FAQ page with a list of frequently asked questions.
    """
    return render(request, 'nest/home.html')

def agent(request):
    """
    Renders an FAQ page with a list of frequently asked questions.
    """
    return render(request, 'nest/agent.html')

def blog(request):
    """
    Renders an FAQ page with a list of frequently asked questions.
    """
    return render(request, 'nest/blog.html')

def contact(request):
    """
    Renders an FAQ page with a list of frequently asked questions.
    """
    return render(request, 'nest/contact.html')

def properties(request):
    """
    Renders an FAQ page with a list of frequently asked questions.
    """
    return render(request, 'nest/properties.html')