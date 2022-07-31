from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core import serializers

from add.models import Knowledge
from .forms import Input

# Create your views here.
def startView(request):
        data = Knowledge.objects.all()
        form = Input
        return render(request, 'start.html', {'knowledges': data, 'form': form})
