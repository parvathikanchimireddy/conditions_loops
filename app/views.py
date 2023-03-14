from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':120,'b':200,'c':400,}
    return render(request,'conditions.html',d)
def loops(request):
    d={'name':'Nithish'}
    return render(request,'loops.html',d)
