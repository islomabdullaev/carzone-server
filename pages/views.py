from django.shortcuts import render

from cars.models import Car
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by("-created_at").filter(is_featured=True)
    cars = Car.objects.all()
    context = {
        "teams": teams,
        "featured_cars": featured_cars,
        "cars": cars,

    }
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Team.objects.all()
    context = {
        "teams": teams,
    }
    return render(request, 'pages/about.html', context)


def services(request):
    return render(request, 'pages/services.html')


def contacts(request):
    return render(request, 'pages/contact.html')
