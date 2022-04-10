from django.shortcuts import render,HttpResponse

# Create your views here.

def comment(request):
     return render(request,'index.html')