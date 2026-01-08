from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    if request.method == "GET":
        return render(request, 'calculator/add.html')
    else:
        fn = int(request.POST.get('num1'))
        sn = int(request.POST.get('num2'))
        res = fn + sn
        data = { 
            'firstnum': fn,
            'secondnum': sn,
            'result': res
        }
        return render(request, 'calculator/add.html', data)

def factorial(request):
    if request.method == "GET":
        return render(request, 'calculator/factorial.html')
    else:
        num = int(request.POST.get('number'))
        fact = 1
        for i in range(1, num + 1):
            fact = fact*i
        data = {
            'number': num,
            'result': fact
        }
        return render(request, 'calculator/factorial.html', data)