from django.shortcuts import render
from .models import Fruits
import json

# Create your views here.
def index(request):
    return render(request, 'visa/index.html', context)
