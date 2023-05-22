from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')
def bruchetta(request):
    return render(request,'bruchetta.html')
def greeksalad(request):
    return render(request,'greeksalad.html')
def grillefish(request):
    return render(request,'grillefish.html')
def lemondissert(request):
    return render(request,'lemondissert.html')