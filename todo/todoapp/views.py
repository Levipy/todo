from django.shortcuts import render
from .models import TodoModel


# Create your views here.

def demo(request):
    todall = TodoModel.objects.all()
    todotrue = TodoModel.objects.filter(todo_status=True)
    todofalse = TodoModel.objects.filter(todo_status=False)
    print(todofalse)

    return render(request, 'index.html', {'todotrue': todotrue}, {'todofalse': todofalse}, {'index': 'index'})


def index(request):
    a = 'aaaaaaaa'
    todofalse = TodoModel.objects.filter(todo_status=False)
    todotrue = TodoModel.objects.filter(todo_status=True)
    print(todofalse)
    print(todotrue)
    return render(request, 'index.html', {'a': a}, {'todotrue': todotrue})
