from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to HomePage")

def contact(request):
    return HttpResponse("Welcome to ContactsPage")

def gallery(request):
    return HttpResponse("Welcome to GalleryPage")

def about(request):
    return HttpResponse("Welcome to AboutPage")
