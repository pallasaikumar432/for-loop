from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'sai','age':21}
    return render(request,'forloop.html',d)