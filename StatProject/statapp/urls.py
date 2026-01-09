from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('display/', views.display, name='display'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact')
]
