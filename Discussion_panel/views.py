from django.shortcuts import redirect,render

def discussion(request):
     return render(request,'discuss.html')
