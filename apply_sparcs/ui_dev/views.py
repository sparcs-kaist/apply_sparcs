from django import template
from django.http import HttpResponse
from django.shortcuts import render

def simple(request, path, ext=None):
    filename = path
    print(path)
    print(ext)

    if ext == None:
        if path == '' or path[-1] == '/':
            filename += 'index.html'
        try:
            res = render(request, filename)
        except IsADirectoryError:
            try:
                filename = path + '/index.html'
                res = render(request, filename)
            except (template.TemplateDoesNotExist, PermissionError):
                res = render(request, '404.html')
        except template.TemplateDoesNotExist:
            try:
                filename = path + '.html'
                res = render(request, filename)
            except template.TemplateDoesNotExist:
                res = render(request, '404.html')
    elif ext == 'html':
        try:
            res = render(request, filename + '.' + ext)
        except template.TemplateDoesNotExist:
            res = render(request, '404.html')
    else:
        res = HttpResponse(status=400)


    return res
