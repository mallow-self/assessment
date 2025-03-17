from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def list(request):
    return JsonResponse({"Message":"welcome to todo!"})