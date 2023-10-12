from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, "blog.html")

def post_1(request):
    return render(request, "post-1.html")

def post_2(request):
    return render(request, "post-2.html")