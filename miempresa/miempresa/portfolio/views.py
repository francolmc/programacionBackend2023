from django.shortcuts import render

# Create your views here.
def portfolio_home(request):
    return render(request, "portfolio-home.html")

def portfolio_about(request):
    return render(request, "portfolio-about.html")

def portfolio_contact(request):
    return render(request, "portfolio-contact.html")