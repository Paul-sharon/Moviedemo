from django.shortcuts import render

def inherit(request):
    return render(request,'inherit.html')

def create(request):
    if request.method == "POST":
        print(request.POST.get('title'))
        print(request.POST.get('year'))
    return render(request, 'create.html')

def edit(request):
    return render(request,'edit.html')

def list(request):
    return render(request,'list.html')


