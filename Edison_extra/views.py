from django.shortcuts import render
from .sense import kashpirovskiy ,houdini, david_blaine


def home(request):
    return render(request,'home.html')

def start(request):
    return render(request,'start.html')

def extra(request):
    user_number = request.GET['user_number']
    kashpirovskiy.abracadabra(user_number)
    print(kashpirovskiy.number)
    return render(request,'extra.html', {'user_number':user_number, 'kash_accuracy':kashpirovskiy.sense_level})


