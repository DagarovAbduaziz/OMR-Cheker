from django.shortcuts import render
from rest_framework import generics
from .models import ApiModel
from .serializers import CoreSerializers
from django.http import JsonResponse
from .Main import cheking

answer = [0, 3, 1, 1, 3, 0, 3, 2, 0, 3, 1, 0, 3, 2, 1, 3, 1, 2, 1, 3]
img = 'n.png'

def createApi(request):
    grading = cheking(img, answer)
    count_true = grading.count(1)
    count_false = grading.count(0)
    count_none = grading.count(None)

    score = count_true / len(grading) * 100

    return JsonResponse({'To`ri javob' : count_true, 'Xato javob' : count_false, 'Belgilanmagan' : count_none, " O'zlashtirish" : score})
