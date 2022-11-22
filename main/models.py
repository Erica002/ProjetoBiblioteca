from django.db import models

# Create your models here.
CLASSES_CHOICES = [
        ('APROVADO', 'APROVADO'),
        ('REJEITADO', 'REJEITADO'),
        ('DEVOLVIDO', 'DEVOLVIDO'),
    ]

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=350)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=100) 
    autor = models.CharField(max_length=120)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    periodo = models.CharField(max_length=10)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_entrega = models.DateField()
    livro = models.ManyToManyField(Livro)
    status_emprestimo = models.CharField(max_length=150,choices=CLASSES_CHOICES)

    def __str__(self):
        return self.periodo