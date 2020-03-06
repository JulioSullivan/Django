from django.shortcuts import render

# Create your views here.
def home(request):
    return request(request, "core/home.html")

def about(request):
    return request(request, "core/about.html")

def services(request):
    return request(request, "core/services.html")

def store(request):
    return request(request, "core/store.html")

def contact(request):
    return request(request, "core/contact.html")

def blog(request):
    return request(request, "core/blog.html")

def sample(request):
    return request(request, "core/sample.html")