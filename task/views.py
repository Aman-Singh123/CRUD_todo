from django.shortcuts import render,redirect
from .models import Todo_item
from .form import TodoForm,updateform
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
import datetime
@csrf_exempt
def create_todo(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form=TodoForm()
    return render(request,'task/todos.html',{'form':form})

@csrf_exempt
def read_data(request):
    todo=Todo_item.objects.values()
    return JsonResponse(list(todo),safe=False)


@csrf_exempt
def update_todo(request,id):
    form=updateform(request.POST)
    if request.method=='POST':
        if form.is_valid():
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            is_done=form.cleaned_data['is_done']
            reg=Todo_item(id=id,title=title,content=content,is_done=is_done)
            reg.save()
            return HttpResponse("data is uipdated")
        else:
            return HttpResponse(' not updated ')    
    return render(request,'task/todos.html',{'form':form})
    
    
