from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "mcl_portfolio/index_page.html")

def projects(request):
    return render(request, "mcl_portfolio/projects_page.html")

def achievements(request):
    return render(request, "mcl_portfolio/achievements_page.html")

def report(request):
    return render(request, "mcl_portfolio/report_page.html")

