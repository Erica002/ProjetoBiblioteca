from django.shortcuts import render, redirect
from .models import Livro, Aluno, Emprestimo
from .forms import LivroForm, EmprestimoForm, AlunoForm

# Create your views here.
def livroList(request):  
    livros = Livro.objects.all()  
    return render(request,"livro-list.html",{'livros':livros})  

def livroCreate(request):  
    if request.method == "POST":  
        form = LivroForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('livro-list')  
            except:  
                pass  
    else:  
        form = LivroForm()  
    return render(request,'livro-create.html',{'form':form})  

def livroUpdate(request, id):  
    livro = Livro.objects.get(id=id)
    form = LivroForm(initial={'titulo': livro.titulo, 'autor': livro.autor, 'genero': livro.genero, 'paginas': livro.paginas})
    if request.method == "POST":  
        form = LivroForm(request.POST, instance=livro)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/livro-list')  
            except Exception as e: 
                pass    
    return render(request,'livro-update.html',{'form':form})  

def livroDelete(request, id):
    livro = Livro.objects.get(id=id)
    try:
        livro.delete()
    except:
        pass
    return redirect('livro-list')

def alunoList(request):  
    alunos = Aluno.objects.all()  
    return render(request,"aluno-list.html",{'alunos':alunos}) 

def alunoCreate(request):  
    if request.method == "POST":  
        form = AlunoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('aluno-list')  
            except:  
                pass  
    else:  
        form = AlunoForm()  
    return render(request,'aluno-create.html',{'form':form})  

def alunoUpdate(request, id):  
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(initial={'nome': aluno.nome, 'matricula': aluno.matricula, 'email': aluno.email, 'endereco': aluno.endereco, 'cidade': aluno.cidade, 'telefone': aluno.telefone})
    if request.method == "POST":  
        form = AlunoForm(request.POST, instance=aluno)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/aluno-list')  
            except Exception as e: 
                pass    
    return render(request,'aluno-update.html',{'form':form})  


def alunoDelete(request, id):
    aluno = Aluno.objects.get(id=id)
    try:
        aluno.delete()
    except:
        pass
    return redirect('aluno-list')
    
def emprestimoList(request):  
    emprestimos = Emprestimo.objects.all()  
    return render(request,"emprestimo-list.html",{'emprestimos':emprestimos}) 

def emprestimoCreate(request):  
    if request.method == "POST":  
        form = EmprestimoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('emprestimo-list')  
            except:  
                pass  
    else:  
        form = EmprestimoForm()  
    return render(request,'emprestimo-create.html',{'form':form}) 

def emprestimoDelete(request, id):
    emprestimo = Emprestimo.objects.get(id=id)
    try:
        emprestimo.delete()
    except:
        pass
    return redirect('emprestimo-list')