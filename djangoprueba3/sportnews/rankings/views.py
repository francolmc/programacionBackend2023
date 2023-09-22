from django.shortcuts import render

# Create your views here.
def rankings_home(request):
    return render(request, "home-rankings.html")