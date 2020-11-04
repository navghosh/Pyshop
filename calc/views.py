from django.shortcuts import render

# Create your views here.
def calc(request):
    return render(request, 'calc.html', {'name':calc})

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']

    res = val1 + val2
    return render(request, 'result.html', {'result':res})