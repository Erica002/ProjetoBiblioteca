from . import views
from django.urls import path

urlpatterns = [    
    path('livro-list', views.livroList, name='livro-list'),
    path('livro-create', views.livroCreate, name='livro-create'),
    path('livro-update/<int:id>', views.livroUpdate, name='livro-update'),
    path('livro-delete/<int:id>', views.livroDelete, name='livro-delete'),
    path('aluno-list', views.alunoList, name='aluno-list'),
    path('aluno-create', views.alunoCreate, name='aluno-create'),
    path('aluno-update/<int:id>', views.alunoUpdate, name='aluno-update'),
    path('aluno-delete/<int:id>', views.alunoDelete, name='aluno-delete'),
    path('emprestimo-list', views.emprestimoList, name='emprestimo-list'),
    path('emprestimo-create', views.emprestimoCreate, name='emprestimo-create'),
    path('emprestimo-delete/<int:id>', views.emprestimoDelete, name='emprestimo-delete'),
]