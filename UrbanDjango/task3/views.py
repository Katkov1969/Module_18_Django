from django.shortcuts import render

from django.shortcuts import render

def main_page(request):
    return render(request, 'third_task/main_page.html')

def second_page(request):
    return render(request, 'third_task/second_page.html')

def third_page(request):
    return render(request, 'third_task/third_page.html')


# Create your views here.
