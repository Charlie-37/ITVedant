from django.shortcuts import HttpResponse


def home(request):
    a='''
    <h1> Welcome Django Web Development</h1>
    <h2><a href="data">First</a></h2>
    <h2><a href="demo">Second</a></h2>
    '''
    return HttpResponse(a)

def first_call(request):
    a='''
    <h1> First Call By Django Project</h1>
    <h1><a href="/">Home</a></h1>
    '''
    return HttpResponse(a)

def second_call(request):
    a='''
    <h1> Second Call By Django Project</h1>
    <h1><a href="/">Home</a></h1>
    '''
    return HttpResponse(a
                        )
