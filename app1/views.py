from django.shortcuts import render


def base(request):
    return render(request,'app1/home.html')
