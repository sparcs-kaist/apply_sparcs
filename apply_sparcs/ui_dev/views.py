from django import template
from django.http import HttpResponse
from django.shortcuts import render
import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
        if path == '' or path[-1] == '/':
            filename += 'index'
        context = getContextFromFilename(filename)

        try:
            res = render(request, filename + '.html', context)

        except template.TemplateDoesNotExist as e:
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
    BASE_DIR = ROOT_DIR + '/frontend/web/'
    try:
        with open(BASE_DIR + filename + '.context.json') as context_data:
            context = json.load(context_data)
    except FileNotFoundError as e:
        print('FileNotFoundError')
        print(e)
        context = {}
    except json.decoder.JSONDecodeError as e:
        print('DecodeError')
        print(e)
        context = None
    print(context)
    return context
