from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'index.html')
    
def explore(request):
    return render(request,'explore.html')
