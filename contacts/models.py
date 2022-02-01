from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    customer_needs_choices = (
        ("I'm interested in this", "I'm interested in this"),
        ("I'd like to know your best price for this", "I'd like to know your best price for this"),
        ("I'd like to test drive this", "I'd like to test drive this"),
        ("I'd like a history report for this", "I'd like a history report for this"),
    )

    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    customer_need = models.CharField(choices=customer_needs_choices, max_length=256)
    car_title = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=56)
    message = RichTextField(blank=True)

    user_id = models.IntegerField(blank=True)
    car_id = models.IntegerField(blank=True)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    fullname = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    subject = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = RichTextField()

    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
