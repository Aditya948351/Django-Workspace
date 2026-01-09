from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def add(request):
    if request.method == 'GET':
        form = StudentForm()
        data = {'form': form}
        return render(request,'add.html',data)
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rollno = form.cleaned_data['rollno']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            data = {
                'name': name,
                'rollno': rollno,
                'phone': phone,
                'email': email
            }
            return render(request, 'display.html', data)
        else:
            data = {'form': form}
            return render(request, 'add.html', data)