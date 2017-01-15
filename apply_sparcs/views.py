from django.shortcuts import render


def init(request):
    return render(request, 'init.html')
