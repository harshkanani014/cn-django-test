from django.shortcuts import render
from django.http import HttpResponse
# from .tasks import test_task
from decouple import config
# Create your views here.

def index(request):
    # test_task.delay()
    large_list = []
    for i in range(100):   
        large_list.append("hello world" * 10)  # Create a large string and append to the list

    total_length = sum(len(s) for s in large_list)
    print(large_list)

    return HttpResponse(f'HHM.....Hello World! This is CN Django Test.By - Harsh Kanani aa.....web hooks test harsh kanani webhook testing 123478 - harsh {total_length}')