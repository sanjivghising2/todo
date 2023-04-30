from django.shortcuts import render, HttpResponse

# Create your views here.
def todo(request):
    return render(request, '../templates/index.html')

def edit(request):
    return render(request, '../templates/edit.html')
    
def todosa(request):
    return render(request, '../templates/todosa.html')
