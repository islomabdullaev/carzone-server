from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from contacts.models import Contact


def inquiry(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        state = request.POST["state"]
        customer_need = request.POST["customer_need"]
        user_id = request.POST["user_id"]
        car_id = request.POST["car_id"]
        car_title = request.POST["car_title"]
        message = request.POST["message"]

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                car_id=car_id,
                user_id=user_id
            )
            if has_contacted:
                messages.error(request, "You have already inquired, please wait as soon as the owner responses.")
                return redirect("/cars/" + car_id)

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            city=city,
            state=state,
            customer_need=customer_need,
            user_id=user_id,
            car_id=car_id,
            car_title=car_title,
            message=message,
        )
        contact.save()
        messages.success(request, "Your request has been submitted, we will get back to you soon.")
        return redirect("/cars/" + car_id)
