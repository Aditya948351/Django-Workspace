from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blogapp/home.html')

def create(request):
    return render(request, 'blogapp/create.html')

def display(request):
    return render(request, 'blogapp/display.html') 