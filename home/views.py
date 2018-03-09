from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def get_index(request):
    return render(request, 'home/index.html')

@login_required()
def get_secret(request):
    return render(request, 'home/secret.html')
