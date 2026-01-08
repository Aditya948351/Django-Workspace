from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    if request.method == "GET":
        return render(request, 'studentadd.html')
    else:
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        standard = request.POST.get('Standard')
        section = request.POST.get('section')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')
        # Process the data as needed
        return render(request, 'display.html', {'name': name, 'roll_no': roll_no, 'standard': standard, 'section': section, 'phone': phone, 'email': email})

def display(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        data = {
            'name': name,
            'age': age
        }
        return render(request, 'studentdisplay.html', data)
    else:
        return HttpResponse("Invalid Request")