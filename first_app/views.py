from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_task
# Create your views here.

def index(request):
    test_task.delay()
    return HttpResponse('HHM.....Hello World! This is CN Django Test.By - Harsh Kanani .....web hooks taaest harsh kanani')
