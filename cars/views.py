from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from cars.models import Car


def cars(request):
    inventory_cars = Car.objects.order_by("-created_at")
    paginator = Paginator(inventory_cars, 2)
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)

    search_model = Car.objects.values_list("model", flat=True).distinct()
    search_city = Car.objects.values_list("city", flat=True).distinct()
    search_year = Car.objects.values_list("year", flat=True).distinct()
    search_body_style = Car.objects.values_list("body_style", flat=True).distinct()
    context = {
        "cars": paged_cars,
        "search_model": search_model,
        "search_city": search_city,
        "search_year": search_year,
        "search_body_style": search_body_style,
    }
    return render(request, "cars/cars.html", context)


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, "cars/car_detail.html", {"car": car})


def search(request):
    all_cars = Car.objects.all().order_by("-created_at")
    search_model = Car.objects.values_list("model", flat=True).distinct()
    search_city = Car.objects.values_list("city", flat=True).distinct()
    search_year = Car.objects.values_list("year", flat=True).distinct()
    search_body_style = Car.objects.values_list("body_style", flat=True).distinct()

    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            all_cars = all_cars.filter(car_title__icontains=keyword)

    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            all_cars = all_cars.filter(model__iexact=model)

    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            all_cars = all_cars.filter(city__iexact=city)

    if "year" in request.GET:
        year = request.GET["year"]
        if year:
            all_cars = all_cars.filter(year__iexact=year)

    if "body_style" in request.GET:
        body_style = request.GET["body_style"]
        if body_style:
            all_cars = all_cars.filter(body_style__iexact=body_style)

    if "min_price" in request.GET:
        min_price = request.GET["min_price"]
        max_price = request.GET["max_price"]
        if max_price:
            all_cars = all_cars.filter(price__gte=min_price, price__lte=max_price)
    context = {
        "searched_cars": all_cars,
        "search_model": search_model,
        "search_city": search_city,
        "search_year": search_year,
        "search_body_style": search_body_style,
    }
    return render(request, "cars/search.html", context)
