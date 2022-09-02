from django.shortcuts import render


def index(request):
    template = 'landing/index.html'
    return render(request, template)
