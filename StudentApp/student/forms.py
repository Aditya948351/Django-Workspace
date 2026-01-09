from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    rollno = forms.IntegerField(label="Roll Number", min_value=5)
    phone = forms.CharField(label="Phone Number", max_length=15)
    email = forms.EmailField(label="Email Address")
