from django.shortcuts import render


def main_page(request):

    return render(request, 'fourth_task/main_page.html')

def second_page(request):
    games = ['Шахматы', 'Шашки', 'Нарды', 'Гонки']
    context = {'games': games}
    return render(request, 'fourth_task/second_page.html', context)

def third_page(request):
    return render(request, 'fourth_task/third_page.html')
