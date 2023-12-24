from django.shortcuts import render


def index(request):
    return render(request, 'general/about_club.html')
