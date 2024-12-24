from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'home/index.html')

def horoscope(request):
    zodiac_signs = {
        "Овен": "Будьте готовы к новым вызовам.",
        "Телец": "Сегодня хороший день для финансовых решений.",
        "Близнецы": "Ваше обаяние поможет вам справиться с трудностями.",
        "Рак": "Отдохните и сосредоточьтесь на себе.",
        "Лев": "Вы в центре внимания! Воспользуйтесь этим.",
        "Дева": "Ваши организаторские навыки помогут достичь успеха.",
        "Весы": "Сохраняйте баланс во всём.",
        "Скорпион": "Сегодня ваш день для важного решения.",
        "Стрелец": "Ищите вдохновение вокруг себя.",
        "Козерог": "Ваш труд будет вознаграждён.",
        "Водолей": "Идеи будут востребованы окружающими.",
        "Рыбы": "Доверьтесь своей интуиции."
    }

    sign = request.GET.get("sign")
    if sign in zodiac_signs:
        return JsonResponse({"sign": sign, "horoscope": zodiac_signs[sign]})
    else:
        return JsonResponse({"error": "Знак зодиака не найден"}, status=404)
