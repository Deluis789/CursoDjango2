from django.shortcuts import render
from .forms import ProductForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Guardar la informacion
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'forms': form})  
    else:
        form = ProductForm()
        return render(request, 'index.html', {'forms': form})  
    