from django.shortcuts import render
from .tasks import *

def home(request):
    FormSubmiting.delay()
    Emailsending.delay()
    return render(request, 'index.html')