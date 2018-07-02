from django.shortcuts import render

# Create your views here.
def atendente(request):
     return render(request,"atendente.html",{})  


def medico(request):
     return render(request,"medico.html",{})  