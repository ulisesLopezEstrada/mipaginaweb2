from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(resquest):
    projects = Project.objects.all()
    return render(resquest,"portfolio/portfolio.html", {'projects': projects})