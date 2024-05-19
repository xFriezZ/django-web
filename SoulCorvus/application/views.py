from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import FormView


@login_required
def first(request):
    return render(request, 'application/first.html')
