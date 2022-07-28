from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def startView(request):
   
        return render(request, 'start.html')
