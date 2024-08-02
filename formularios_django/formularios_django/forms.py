from django import forms

class CommentForm(forms.Form):
    nombre = forms.CharField(label='Escribe tu nombre', max_length=50, help_text='50 caracteres maximo')
    url = forms.URLField(label='Tu sitio web', required=False, initial='http://')
    comment = forms.CharField()

class ContactForm(forms.Form):
    nombres = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean_nombres(self):
        nombre = self.cleaned_data.get('nombres')
        if nombre != 'juan':
            raise forms.ValidationError('Tan solo esta permitido a Juan')
        else:
            return nombre

