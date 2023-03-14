from django.shortcuts import render

# Create your views here.
def evens(request):
    d={'movie':'thor the dark world','a':22}
    return render(request,'evens.html',context=d)
