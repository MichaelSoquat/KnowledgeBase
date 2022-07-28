from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def legal_notice_view(request):
    return render(request, 'legal_notice.html')