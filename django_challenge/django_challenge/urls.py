"""django_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('base.urls')),
    path('challenge-1/', include('challenge_1.urls')),
    path('challenge-2/', include('challenge_2.urls')),
    path('challenge-3/', include('challenge_3.urls')),
    path('challenge-4/', include('challenge_4.urls')),
    path('challenge-5/', include('challenge_5.urls')),
    path('challenge-6/', include('challenge_6.urls')),
]
