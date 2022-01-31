from django.urls import path

from cars import views

urlpatterns = [
    path("", views.cars, name="cars"),
    path("<int:pk>/", views.car_detail, name="detail"),
    path("search/", views.search, name="search"),
]
