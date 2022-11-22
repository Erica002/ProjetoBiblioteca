from django.forms import CharField, ModelForm
from .models import Livro, Aluno, Emprestimo
from django import forms

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "autor", "genero", "paginas"]

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'

        widgets = {
            'livro': forms.CheckboxSelectMultiple(),
            'data_emprestimo': forms.TimeInput(attrs={'type': 'date'}),
            'data_entrega': forms.TimeInput(attrs={'type': 'date'}),
        }

    