from django.shortcuts import render
from .forms import ClientForm
# Create your views here.

def index(request):
    error = ''
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Некоректное заполнение'
    return render(request, 'main.html', {'form':ClientForm(), 'error':error})