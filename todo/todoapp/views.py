from django.shortcuts import render
from .models import TodoModel
# Create your views here.

def demo(request):
    todall = TodoModel.objects.all()
    todotrue = TodoModel.objects.filter(todo_status = True)
    todofalse = TodoModel.objects.filter(todo_status = False)
    print(todofalse)


    return render(request,'demo.html',{'todotrue':todotrue},{'todofalse':todofalse})
