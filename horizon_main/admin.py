from django.contrib import admin

from horizon_main.models import Property, RequestViewing, ContactRequest


# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', "price", 'listed_at']
    list_per_page = 25
    list_filter = ['listed_at']
    search_fields = ['name', 'location']


@admin.register(RequestViewing)
class RequestViewingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'property', 'preferred_date', 'is_viewed']
    list_per_page = 25
    list_filter = ['is_viewed', 'preferred_date']
    search_fields = ['property', 'user']


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'title']
    list_per_page = 25
    list_filter = ['created_at']
    search_fields = ['title', 'email', 'name']