from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html',{'name':'Ajay'})
def add(request):
    n1 = request.POST['n1']
    n2 = request.POST['n2']
    tot = int(n1)+int(n2)
    return render(request,'result.html',{'total':tot}) 