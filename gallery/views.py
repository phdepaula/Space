from django.shortcuts import render

def index(request):
    """Index Route"""
    return render(request, "gallery/index.html")

def star(request):
    """Star Route"""
    return render(request, "gallery/star.html")

def galaxy(request):
    """Galaxy Route"""
    return render(request, "gallery/galaxy.html")

def nebula(request):
    """Nebula Route"""
    return render(request, "gallery/nebula.html")

def planet(request):
    """Planet Route"""
    return render(request, "gallery/planet.html")
