"""solvers URL Configuration

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
from django.urls import path

import minimaxsumgame.views
import minimaxsumgame.api_views

import beautifultripletsgame.views

urlpatterns = [
    path('minimaxsumgame', minimaxsumgame.views.show, name='get-answer'),
    path('beautripletsgame',beautifultripletsgame.views.show, name='beautiful-view'),
    path('beautripletsjson',beautifultripletsgame.views.index, name='beautiful-json'),
    path('', minimaxsumgame.views.index, name='list-products'),
    path('admin/', admin.site.urls),
]
