from django.shortcuts import render


def medico(request):
     return render(request,"medico.html",{})  