from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_html(request):
    users = ['Kate', "Tom", "Alex"]
    info = {}
    context = {
        "info": info,
    }
    if request.method == 'POST':
        #Получение данных
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users:
            info.update({'error': "Пользователь уже существует!"})
            return HttpResponse(info.get('error'))
        elif password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
            return HttpResponse(info.get('error'))
        elif int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18!'})
            return HttpResponse(info.get('error'))
        else:
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'fifth_task/registration_page.html', context)

def sign_up_by_django(request):
    users = ['Kate', "Tom", "Alex"]
    info ={}
    context = {
        "info": info,
    }

    if request.method == "POST":
        form = UserRegister(request.POST)
        info.update({"form": form})

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

        if username in users:
            info.update({'error': "Пользователь уже существует!"})
            return HttpResponse(info.get('error'))
        elif password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
            return HttpResponse(info.get('error'))
        elif int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18!'})
            return HttpResponse(info.get('error'))
        else:
            return HttpResponse(f"Приветствуем, {username}!")

    form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context)










