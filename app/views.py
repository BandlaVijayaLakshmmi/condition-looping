from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    d={'a':30}
    return render(request,'ifcondition.html',context=d)
def ifelse(request):
    d={'a':30,'b':40}
    return render(request,'if_else.html',context=d)
def ifelifelse(request):
    d={'a':30,'b':50,'c':60}
    return render(request,'if_elif_else.html',context=d)
def nestedif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'nestedif.html',context=d)
def looping(request):
    d={'name':'vicky'}
    return render(request,'looping.html',context=d)