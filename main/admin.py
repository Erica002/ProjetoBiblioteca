from django.contrib import admin
from main.models import Aluno, Genero, Livro, Emprestimo


# Register your models here.
admin.site.register(Aluno)
admin.site.register(Genero)
admin.site.register(Livro)
admin.site.register(Emprestimo)