from django.contrib import admin

from contacts.models import Contact, ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "car_title", "city", "state", "created_at")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "email", "car_title")
    list_per_page = 25


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "email", "created_at")
    list_display_links = ("id", "fullname")
    search_fields = ("first_name", "fullname", "email")


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactUs, ContactUsAdmin)

