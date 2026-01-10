from django.urls import path
from . import views

urlpatterns = [
    path('studentlist/', views.studentlist, name='studentlist'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('updatestudent/<int:id>/', views.updatestudent, name='updatestudent'),
    path('deletestudent/<int:id>/',views.deletestudent,name='deletestudent')
]