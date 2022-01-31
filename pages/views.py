from django.shortcuts import render

from cars.models import Car
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by("-created_at").filter(is_featured=True)
    cars = Car.objects.all()

    search_model = Car.objects.values_list("model", flat=True).distinct()
    search_city = Car.objects.values_list("city", flat=True).distinct()
    search_year = Car.objects.values_list("year", flat=True).distinct()
    search_body_style = Car.objects.values_list("body_style", flat=True).distinct()
    context = {
        "teams": teams,
        "featured_cars": featured_cars,
        "cars": cars,
        "search_model": search_model,
        "search_city": search_city,
        "search_year": search_year,
        "search_body_style": search_body_style,
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
