from django.shortcuts import redirect, render

from . models import *

# Create your views here.
def Home(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        todo = Todo.objects.create(title=title,description=description,startdate=startdate,enddate=enddate)
        todo.save()
    todoitems = Todo.objects.all()    
    return render (request,'home.html',{'to':todoitems})

def delete(request,id):
    todo =Todo.objects.get(id=id)
    todo.delete()
    return redirect('items')

def Todoitems(request):
     todoitems = Todo.objects.all()
    
     return render(request, 'items.html', {'to': todoitems})