from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm

# My imports
from django.http import HttpResponse
import datetime


# Create your views here.

def home(request):
    # return on template option
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

    # exemplo de variáveis dentro do html
    data = {
        'now': datetime.datetime.now(),
        'transacoes': ['t1', 't2', 't3']
    }

    return render(request, 'contas/home.html', data)


def listagem(request):

    data = {
        'transacoes': Transacao.objects.all()
    }

    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data = {
        'form': form
    }
    return render(request, 'contas/form.html', data)
