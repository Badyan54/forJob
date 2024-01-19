from django.shortcuts import render, redirect
from .models import DB_output

def index(request):
    if request.method == 'POST':
        return redirect("data")

    return render(request, 'main/index.html')

def data(request):
    values = DB_output.objects.all()
    return render(request, 'main/data.html', {'values': values,})