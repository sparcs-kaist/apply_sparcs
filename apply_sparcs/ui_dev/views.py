from django import template
from django.http import HttpResponse
from django.shortcuts import render
import json

def simple(request, path, ext=None):
    filename = path
    print(path)
    print(ext)

    # if ext == None:
    #     if path == '' or path[-1] == '/':
    #         filename += 'index'
    #     context = getContextFromFilename(filename)
    #     try:
    #         res = render(request, filename + '.html', context)
    #     except IsADirectoryError:
    #         try:
    #             print(path)
    #             filename = path + '/index'
    #             print(filename)
    #             res = render(request, filename + '.html')
    #         except (template.TemplateDoesNotExist, PermissionError):
    #             res = render(request, '404.html')
    #     except template.TemplateDoesNotExist:
    #         try:
    #             filename = path + '.html'
    #             res = render(request, filename)
    #         except template.TemplateDoesNotExist:
    #             res = render(request, '404.html')
    # elif ext == 'html':
    #     try:
    #         res = render(request, filename + '.' + ext)
    #     except template.TemplateDoesNotExist:
    #         res = render(request, '404.html')
    # else:
    #     res = HttpResponse(status=400)


    if ext == None:
        filename = path
        print (filename)
        if path == '' or path[-1] == '/':
            filename += 'index'
        context = getContextFromFilename(filename)
        print (filename)
        print (context)
        try:
            res = render(request, filename + '.html', context)
        except template.TemplateDoesNotExist as e:
            print('except')
            try:
                filename = path + '/index'
                context = getContextFromFilename(filename)
                res = render(request, filename + '.html', context)
            except template.TemplateDoesNotExist:
                res = render(request, '404.html')
    elif ext == 'html':
        filename = path
        context = getContextFromFilename(filename)
        try:
            res = render(request, filename + '.html', context)
        except template.TemplateDoesNotExist:
            res = render(request, '404.html')
    else:
        res = HttpResponse(status=400)

    return res

def getContextFromFilename(filename):
    '''
        컨텍스트 파일을 불러온다.
    '''
    try:
        with open(filename + '.context.json') as context_data:
            context = json.load(context_data)
    except FileNotFoundError as e:
        # print(e)
        context = {}
    except json.decoder.JSONDecodeError as e:
        context = None
        # print(e)
    return context
