from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'available_seats')  # Customize this as needed
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate slug from title

admin.site.register(Event, EventAdmin)
