from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def about(request):
    return HttpResponse("This is the About page.")

def contact(request):
    return HttpResponse("This is the Contact page.")

def gallery(request):
    return HttpResponse("This is the Gallery page.")