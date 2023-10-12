"""
URL configuration for comunicados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webhome import views as webhome
from blog import views as blog

urlpatterns = [
    path('', webhome.home, name="home"),
    path('about/', webhome.about, name="about"),
    path('blog/', blog.blog, name="blog"),
    path('blog/post-1', blog.post_1, name="post-1"),
    path('blog/post-2', blog.post_2, name="post-2"),
    path('admin/', admin.site.urls),
]
