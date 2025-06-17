from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from .views import TechView

urlpatterns = [
    path('', views.home, name='home'),
    path('tech/', TechView.as_view(), name='tech'),    
    path('ghs/', views.ghs, name='ghs'),
    path('photography/', views.photography, name='photography'),
]