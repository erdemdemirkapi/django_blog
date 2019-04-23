from django.shortcuts import render, HttpResponse

def post_index(request):
    return HttpResponse('index')

def post_detail(request):
    return HttpResponse('detail')

def post_create(request):
    return HttpResponse('create')

def post_update(request):
    return HttpResponse('update')

def post_delete(request):
    return HttpResponse('delete')