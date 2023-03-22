from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pessoaView(request):
    return render(request, 'usuarios/pessoa_view.html')