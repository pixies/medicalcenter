from django.shortcuts import render


def paciente(request):
     return render(request,"paciente.html",{})  