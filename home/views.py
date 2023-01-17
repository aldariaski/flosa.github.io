from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import time

def home(request):

    context = {"doc": "doc",
               "isi": "isi"}
    if request.method == "POST":
        query = request.POST.get('search')
        return render(request, 'home/home.html', context)

    return render(request, 'home/home.html', context)