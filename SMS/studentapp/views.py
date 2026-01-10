from django.shortcuts import get_object_or_404, render, redirect
from .models import Student

# Create your views here.
def studentlist(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request,'studentlist.html',{'students':students})

def addstudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        rollno = request.POST['rollno']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        st = Student()
        st.name = name
        st.roll = rollno
        st.age = age
        st.phone = phone
        st.email = email
        st.address = address
        st.save()
        # return render(request,'studentlist.html')
        return redirect('studentlist')
    
    else:
        return render(request,'addstudent.html')

def updatestudent(request,id):
    st = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        rollno = request.POST['rollno']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        st.name = name
        st.rollno = rollno
        st.age = age
        st.phone = phone
        st.email = email
        st.address = address
        st.save()
        # return render(request,'studentlist.html')
        return redirect('studentlist')
    else:
        
        return render(request,'updatestudent.html',{'student':st})
    
def deletestudent(request,id):
    st = get_object_or_404(Student, pk=id)
    st.delete()
    return redirect('studentlist')    