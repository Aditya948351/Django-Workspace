from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('BlogApp.blog_urls'))
]
