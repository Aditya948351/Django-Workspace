from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'authorapp/home.html')
def create(request):
    return render(request, 'authorapp/create.html')
def display(request):
    return render(request, 'authorapp/display.html')