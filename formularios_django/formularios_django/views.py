from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm()
    return render(request, 'form.html', {'comment_forms': comment_form})

def goal(request):
    if request.method != 'POST':
        return HttpResponse('Metodo no permitido')
    
    return HttpResponse(request.POST['nombre'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'forms': form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aqui iran todas las acciones si es verdadero
            return HttpResponse('Valido')
        else: 
            # Aqui irian las acciones cuando sea falso
            return render(request, 'widget.html', {'forms': form})