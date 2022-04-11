from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'index.html')
    
def explore(request):
    return render(request,'explore.html')

def self_help(request):
    return render(request,'self-help.html')

def bloglist(request):
    return render(request,'bloglist.html')